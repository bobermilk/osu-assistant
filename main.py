from genericpath import isdir
import shutil
import webbrowser
import wx
from api import check_cookies, get_token
import gui
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine
import asyncio
import data, constants, misc, database
from download import destroy_client
from pubsub import pub
from strings import generate_beatmap_name, generate_collection_name
import os

app = WxAsyncApp()

# Used to allow updating of ui from outside using pub.sendMessage()
def update_sources():
    main_window.update_sources(None)

def update_activity():
    main_window.update_activity(None)

def update_progress(value, range, progress_message):
    if range != None:
        # set job count to range
        main_window.m_progressbar.SetRange(range)
    if value != None:  
        # Set current job progress
        main_window.m_progressbar.SetValue(value)
    else:
        # Job complete
        main_window.m_progressbar.SetRange(0)
    if progress_message != None:
        main_window.m_activity_progress.SetLabelText(progress_message)

def enable_job_toggle_button():
    # called when you are allowed to stop jobs
    main_window.m_toggle_downloading.Enable()

def reset_job_toggle_button_text():
    # called when jobs are completed
    main_window.m_toggle_downloading.SetLabelText(constants.activity_start)

def show_dialog(msg, ok=None):
    # called when new release dropped on github
    dlg = wx.MessageDialog(main_window, 
        msg,
        "Ok", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
    result = dlg.ShowModal()
    if result == wx.ID_OK:
        if ok != None:
            ok()
    dlg.Destroy()
    return result == wx.ID_OK

class MainWindow(gui.Main):
    """
    Main window bro
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.Maximize(True)
        self.m_version.SetLabelText("App version: {}".format(constants.APP_VERSION))
        pub.subscribe(update_sources, "update.sources")
        pub.subscribe(update_activity, "update.activity")
        pub.subscribe(update_progress, "update.progress")
        pub.subscribe(enable_job_toggle_button, "enable.job_toggle_button")
        pub.subscribe(reset_job_toggle_button_text, "reset.job_toggle_button_text")
        pub.subscribe(show_dialog, "show.dialog")
        AsyncBind(wx.EVT_BUTTON, self.show_add_window, self.m_add_source)
        AsyncBind(wx.EVT_BUTTON, self.toggle_jobs, self.m_toggle_downloading)
        AsyncBind(wx.EVT_BUTTON, self.update_settings, self.m_save_settings)
        AsyncBind(wx.EVT_CLOSE, self.onDestroy, self)

    async def onDestroy(self, event):
        if show_dialog("Are you sure you want to close osu assistant?"):
            # pickle the data
            await destroy_client()
            data.save_data()      
            
            if add_source_window!=None:
                add_source_window.Destroy()
            self.Destroy()

    # used to repopulate the source list after a edit
    def update_sources(self, event):
        self.m_source_list.DeleteAllPages()
        source_list=data.get_sources().read()
        for source_key, source in source_list:
            source_panel=gui.ListPanel(self.m_source_list)
            for i, beatmap in enumerate(source.get_available_beatmaps()):
                source_panel.m_list.Insert("beatmapset_id="+str(beatmap[0]) + " beatmap_id="+str(beatmap[1])+" checksum="+str(beatmap[2]),i)
            for i, beatmap in enumerate(source.get_unavailable_beatmaps()):
                source_panel.m_list.Insert("beatmapset_id="+str(beatmap[0]) + " beatmap_id="+str(beatmap[1]) +" checksum="+str(beatmap[2])+ " (unavailable for download)",i)
            for i, beatmap in enumerate(source.get_missing_beatmaps()):
                source_panel.m_list.Insert("beatmapset_id="+str(beatmap[0]) + " beatmap_id="+str(beatmap[1]) +" checksum="+str(beatmap[2])+  " (missing)",i)
            self.m_source_list.AddPage(source_panel, f"★ Collection {generate_collection_name(data.get_sources().collection_index[source_key])}: {source_key}")

    # used to repopulate the activity list after download completes
    def update_activity(self, event):
        self.m_activity_list.Clear()
        job_list=data.get_jobs().read()
        i=0
        while len(job_list) > 0:
            job=job_list.pop(0)
            job_source_key=job.get_job_source_key()
            self.m_activity_list.Insert(str(job_source_key+f" ({job.get_job_downloads_cnt()} beatmaps will be downloaded)"), i)

    def export_collection_to_beatmap(self, event):
        if data.get_settings().valid_osu_directory:
            if os.path.isfile(os.path.join(data.get_settings().osu_install_folder, "collection.db")):
                collection_window=CollectionSelectionWindow()
                collection_window.SetIcon(wx.Icon("assets/osu.ico"))
                collection_window.Show()
            else:
                show_dialog("You have provided a osu install directory, but there is no collection.db in it")
        else:
            show_dialog("You need to set a osu install directory first")

    async def restore_settings(self, event):
        get_token()
        await check_cookies()

        s=data.get_settings()
        if s.osu_install_folder!=None:
            # Initialize the cache db
            await database.create_osudb()
        if s.osu_install_folder != None:
            self.m_osu_dir.SetPath(s.osu_install_folder)
        self.m_client_id.SetHelpText("osu oauth application client id")
        self.m_client_secret.SetHelpText("osu oauth application client secret")
        if s.oauth != None:
            self.m_client_id.SetValue(s.oauth[0])
            self.m_client_secret.SetValue(s.oauth[1])
        else:
            self.m_client_id.SetValue("client_id")
            self.m_client_secret.SetValue("client_secret")
        self.m_autodownload_toggle.SetValue(s.download_on_start)
        self.m_use_osu_mirror.SetValue(s.download_from_osu)
        self.m_settings_xsrf_token.SetHelpText("Inspect element on osu website to obtain")
        self.m_settings_osu_session.SetHelpText("Inspect element on osu website to obtain")
        if s.oauth != None and s.valid_osu_cookies == False:
            show_dialog("XSRF-TOKEN or osu_session provided has expired. You have to replace them")
            self.m_settings_xsrf_token.SetValue("XRSF_TOKEN")
            self.m_settings_osu_session.SetValue("osu_session")
        else:
            self.m_settings_xsrf_token.SetValue("XSRF_TOKEN")
            self.m_settings_osu_session.SetValue("osu_session")
        
        # Refresh sources and jobs (the views will update)
        await data.Sources.refresh()

        # Initiate automatic downloads
        if s.download_on_start:
            pub.sendMessage("toggle.jobs")
            StartCoroutine(self.toggle_jobs, self)
            
    async def update_settings(self, event):
        s=data.get_settings()
        s.osu_install_folder=self.m_osu_dir.GetPath()
        s.oauth=(self.m_client_id.GetValue(), self.m_client_secret.GetValue())
        s.download_on_start=self.m_autodownload_toggle.GetValue()
        s.download_from_osu=self.m_use_osu_mirror.GetValue()
        s.xsrf_token=self.m_settings_xsrf_token.GetValue()
        s.osu_session=self.m_settings_osu_session.GetValue()
        s.download_interval=self.m_download_interval.GetValue()

        if s.osu_install_folder!=None:
            # Initialize the cache db
            await database.create_osudb()

        if s.download_from_osu==True:
            await check_cookies()
        
        data.save_data()      
    
    # toggle jobs
    async def toggle_jobs(self, event=None):
        self.m_toggle_downloading.Disable()
        if self.m_toggle_downloading.GetLabel() == constants.activity_stop:
            data.cancel_jobs_toggle=True
            self.m_toggle_downloading.SetLabelText(constants.activity_start)
        elif not data.cancel_jobs_toggle:
            self.m_toggle_downloading.SetLabelText(constants.activity_stop)
            await data.get_jobs().start_jobs()

    async def show_add_window(self, event):
        global add_source_window
        if data.get_settings().osu_install_folder!=None and data.get_settings().oauth != None:
            add_source_window=AddSourceWindow(parent=None)
            add_source_window.SetIcon(wx.Icon("assets/osu.ico"))
            add_source_window.Show()
            self.m_add_source.Disable()
            await add_source_window.populate_add_window(add_source_window)
        else:
            show_dialog("You must set your osu install folder and do oauth authentication first!")
    
    def open_discord(self, event):
        webbrowser.open(constants.link_discord)
    def open_donate(self, event):
        webbrowser.open(constants.link_paypal)
    def open_github(self, event):
        webbrowser.open(constants.link_github)
    def open_website(self, event):
        webbrowser.open(constants.link_website)
        
class AddSourceWindow(gui.AddSource):
    """
    Window for adding a new source
    """
    def __init__(self, parent=None):
        super(AddSourceWindow, self).__init__(parent)
        # bind the buttons to their respective callbacks
        AsyncBind(wx.EVT_BUTTON, self.add_userpage, self.m_add_userpage)
        AsyncBind(wx.EVT_BUTTON, self.add_tournament, self.m_add_tournament)
        AsyncBind(wx.EVT_BUTTON, self.add_mappack, self.m_add_mappack)
        AsyncBind(wx.EVT_BUTTON, self.add_osucollector, self.m_add_osucollector)
        AsyncBind(wx.EVT_CHOICE, self.change_mappack_section, self.m_mappack_section)
        AsyncBind(wx.EVT_WINDOW_DESTROY, self.onDestroy, self)

    async def onDestroy(self, event):
        global add_source_window
        global main_window
        add_source_window=None
        #User closed application
        if main_window != None:
            main_window.m_add_source.Enable()

    async def add_userpage(self, event):
        links=self.m_userpages.GetValue()
        scope=[self.m_user_top100.GetValue(), self.m_user_favourites.GetValue(), self.m_user_everything.GetValue(),
                self.m_user_ranked.GetValue(), self.m_user_loved.GetValue(), self.m_user_pending.GetValue(), self.m_user_graveyarded.GetValue()]
        self.Destroy()
        await data.get_sources().add_user_source(links, scope)
        
    async def add_tournament(self, event):
        selection=self.m_tournament.GetPageText(self.m_tournament.GetSelection())
        self.Destroy()
        await data.get_sources().add_tournament_source(selection)

    async def add_mappack(self, event):
        labels=[self.m_mappack_list.GetString(x) for x in self.m_mappack_list.GetSelections()]
        ids=[int(x.split(":")[0]) for x in labels]
        self.Destroy()
        await data.get_sources().add_mappack_source(ids)

    async def add_osucollector(self, event):
        links=self.m_osu_collector.GetValue()
        self.Destroy()
        await data.get_sources().add_osucollector_source(links)

    async def change_mappack_section(self, event):
        selection=str(self.m_mappack_section.GetSelection())
        self.m_mappack_list.Clear()
        i=0
        for source_key, item in data.MappackJson[selection].items():
            source_name=item[0]
            self.m_mappack_list.Insert(f"{source_key}: {source_name} ({len(item[1])} beatmapsets)", i)
            i+=1

    async def populate_add_window(self, event):
        for item in data.TournamentJson.items():
            beatmap_list=[]
            add_tournament_panel=gui.ListPanel(self.m_tournament)
            for beatmap in item[1][1]:
                beatmap_list.append(constants.osu_beatmap_url_full.format(beatmap[0], beatmap[2], beatmap[1]))
            tournament_key=item[0] + ": "+ item[1][0]
            if len(beatmap_list)>0:
                add_tournament_panel.m_list.InsertItems(beatmap_list,0)
            
            self.m_tournament.AddPage(add_tournament_panel, tournament_key)
        
        mappack_list=[]
        for source_key, item in data.MappackJson["0"].items():
            source_name=item[0]
            mappack_list.append(f"{source_key}: {source_name} ({len(item[1])} beatmapsets)")
        if len(mappack_list)>0:
            self.m_mappack_list.InsertItems(mappack_list,0)
    def open_subscribed_mappers(self, event):
        webbrowser.open(constants.link_mappers)

class CollectionSelectionWindow(gui.CollectionsSelection):
    """
    Window for adding a new source
    """
    def __init__(self, parent=None):
        super(CollectionSelectionWindow, self).__init__(parent)
        self.current_collections=database.collection_to_dict()

        if not isinstance(self.current_collections, bool):
            for i, collection in enumerate(self.current_collections["collections"]):
                self.m_collections_selection.Insert(str(f"{i}: {collection['name']}"), i)

    def export_collections_to_beatmap(self, event):
        settings=data.get_settings()
        osudb=database.create_osudb2()
        selections=self.m_collections_selection.GetSelections()
        new_folder=os.path.join(settings.osu_install_folder, "Songs", generate_beatmap_name(8))
        while os.path.isdir(new_folder):
            new_folder=os.path.join(settings.osu_install_folder, "Songs", generate_beatmap_name(8))
            
        os.mkdir(new_folder)
        print(new_folder)
        if len(selections) > 0:
            for i, collection in enumerate(self.current_collections["collections"]):
                if i in selections:
                    for checksum in collection["hashes"]:
                        beatmap_id, song_title, mapper, folder = osudb[checksum]
                        for dirpath, dirnames, filenames in os.walk(os.path.join(settings.osu_install_folder, "Songs", folder)):
                            for filename in filenames:
                                filename=str(filename)
                                if filename.endswith(".osu"):
                                    lines=f.readlines()
                                    found=False
                                    with open(os.path.join(settings.osu_install_folder, "Songs", folder, filename), "r") as f:
                                        for line in lines:
                                            if "BeatmapID:{}".format(beatmap_id) in line:
                                                found=True
                                                break
                                            if "Title:{}".format(song_title) in line and "Creator:{}".format(mapper):
                                                found=True
                                                break
                                    if found:
                                        dest=os.path.join(settings.osu_install_folder, "Songs", new_folder, filename)
                                        with open(dest, "w+"):
                                            pass

            self.Destroy()



                
# Used for AddSourceWindow to call functions in main window
# There can be only one instance at all times
main_window = MainWindow()
add_source_window=None

async def main():
    main_window.SetIcon(wx.Icon("assets/osu.ico"))
    main_window.Show()
    app.SetTopWindow(main_window)
    show_dialog("Note from developer:\n\nThis app has no loading screens and will not respond whenever it's working (including after you click OK)\nYou may join the discord server to report bugs")
    await misc.init()
    await main_window.restore_settings(None)
    await app.MainLoop()

asyncio.run(main())