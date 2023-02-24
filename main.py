import webbrowser
import wx
from api import check_cookies, get_token, get_oauth
import gui
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine
import asyncio
import data, constants, buen, database, misc
from gui_extra import PyBusyInfo
from pubsub import pub
import sys
import os
import aiohttp

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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

def show_dialog(msg, ok=None, focus_main=True):
    focus=main_window
    if not focus_main:
        focus=add_source_window
    # called when new release dropped on github
    dlg = wx.MessageDialog(focus, 
        msg,
        "Alert OwO", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
    result = dlg.ShowModal()
    if result == wx.ID_OK:
        if ok != None:
            ok()
    dlg.Destroy()
    return result == wx.ID_OK

def show_loading(msg):
    global loading
    try:
        loading
        if msg == None:
            del loading
        else: 
            loading.UpdateText(msg)
    except:
        if msg != None:
            loading=PyBusyInfo(msg, parent=main_window, title="Loading UwU")

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
        pub.subscribe(show_loading, "show.loading")
        AsyncBind(wx.EVT_BUTTON, self.show_add_window, self.m_add_source)
        AsyncBind(wx.EVT_BUTTON, self.toggle_jobs, self.m_toggle_downloading)
        AsyncBind(wx.EVT_BUTTON, self.update_settings, self.m_save_settings)
        AsyncBind(wx.EVT_CLOSE, self.onDestroy, self)

    async def onDestroy(self, event):
        if show_dialog("Are you sure you want to close osu assistant?"):
            # pickle the data
            data.save_data()      
            
            if add_source_window!=None:
                add_source_window.Destroy()
            self.Destroy()
            sys.exit(0)

    # used to repopulate the source list after a edit
    def update_sources(self, event):
        self.m_source_list.DeleteAllPages()

        source_list=data.Sources.read()
        for source_key, source in source_list:
            source_panel=ListPanel(self.m_source_list)
            missing_beatmaps=[beatmap[0] for beatmap in source.get_missing_beatmaps()]
            i=0
            for beatmap in source.get_available_beatmaps():
                if beatmap[0] not in missing_beatmaps:
                    source_panel.m_list.Insert("https://osu.ppy.sh/beatmapsets/"+str(beatmap[0]) ,i)
                    i+=1
            for i, beatmap in enumerate(source.get_unavailable_beatmaps()):
                source_panel.m_list.Insert("https://osu.ppy.sh/b/"+str(beatmap[1]) +" (unavailable for download)",i)
            for i, beatmapset_id in enumerate(missing_beatmaps):
                source_panel.m_list.Insert("https://osu.ppy.sh/beatmapsets/"+str(beatmapset_id) +" (missing in-game)",i)
            self.m_source_list.AddPage(source_panel, f"#{data.Sources.collection_index[source_key]}: {source_key}")
        try:
            self.m_source_list.GetListView().SetColumnWidth(0, 750)
            self.m_source_list.GetListView().Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.delete_source)
        except:
            pass

    # used to repopulate the activity list after download completes
    def update_activity(self, event):
        self.m_activity_list.Clear()
        job_list=data.Jobs.read()
        i=0
        while len(job_list) > 0:
            job=job_list.pop(0)
            job_source_key=job.get_job_source_key()
            self.m_activity_list.Insert(str(job_source_key+f" ({job.get_job_downloads_cnt()} beatmaps will be downloaded)"), i)

    def export_collection_to_beatmap(self, event):
        if data.Settings.valid_osu_directory:
            if os.path.isfile(os.path.join(data.Settings.osu_install_folder, "collection.db")):
                # collection_window=CollectionSelectionWindow()
                # collection_window.SetIcon(wx.Icon(resource_path("osu.ico")))
                # collection_window.Show()
                show_dialog("This feature is not implemented yet...")
            else:
                show_dialog("You have provided a osu install directory, but there is no collection.db in it")
        else:
            show_dialog("You need to set a osu install directory first")

    async def restore_settings(self, event):
        get_token()
        async with aiohttp.ClientSession() as session:
            await check_cookies(session)

        s=data.Settings
        if s.osu_install_folder!=None:
            # Initialize the cache db
            StartCoroutine(self.create_osudb, self)
        if s.osu_install_folder != None:
            self.m_osu_dir.SetPath(s.osu_install_folder)
        self.m_autodownload_toggle.SetValue(s.download_on_start)
        self.m_use_osu_mirror.SetValue(s.download_from_osu)
        self.m_settings_xsrf_token.SetHelpText("Inspect element on osu website to obtain")
        self.m_settings_osu_session.SetHelpText("Inspect element on osu website to obtain")
        if s.xsrf_token!="" and s.osu_session!="" and s.valid_osu_cookies == False:
            show_dialog("XSRF-TOKEN or osu_session provided has expired. You have to replace them")
            self.m_settings_xsrf_token.SetValue("XRSF_TOKEN")
            self.m_settings_osu_session.SetValue("osu_session")
        
        # Refresh sources and jobs (the views will update)
        await data.Sources.refresh()
            
    async def update_settings(self, event):
        s=data.Settings
        s.osu_install_folder=self.m_osu_dir.GetPath()
        s.download_on_start=self.m_autodownload_toggle.GetValue()
        s.download_from_osu=self.m_use_osu_mirror.GetValue()
        s.xsrf_token=self.m_settings_xsrf_token.GetValue()
        s.osu_session=self.m_settings_osu_session.GetValue()
        s.download_interval=self.m_download_interval.GetValue()

        if not os.path.isfile(os.path.join(s.osu_install_folder, "osu!.db")):
            show_dialog("Warning: The osu folder you selected is not the osu install directory. If you wish to just download beatmaps to the selected folder without collection updates, this is alright.")

        if s.valid_oauth==False:
            get_token()
        
        if s.osu_install_folder!=None:
            # Initialize the cache db
            StartCoroutine(self.create_osudb, self)

        if s.download_from_osu==True:
            async with aiohttp.ClientSession() as session:
                await check_cookies()
        
        data.save_data()      
    
    # toggle jobs
    async def toggle_jobs(self, event=None):
        self.m_toggle_downloading.Disable()
        if self.m_toggle_downloading.GetLabel() == constants.activity_stop:
            data.cancel_jobs_toggle=True
            self.m_toggle_downloading.SetLabelText(constants.activity_start)
        elif not data.cancel_jobs_toggle:
            if data.Settings.valid_osu_directory:
                self.m_toggle_downloading.SetLabelText(constants.activity_stop)
                await data.Jobs.start_jobs()
            else:
                show_dialog("Set the correct osu install folder in settings!")
                self.m_toggle_downloading.Enable()

    async def show_add_window(self, event):
        global add_source_window
        if data.Settings.valid_oauth == True:
            add_source_window=AddSourceWindow(parent=None)
            add_source_window.SetIcon(wx.Icon(resource_path("osu.ico")))
            add_source_window.Show()
            self.m_add_source.Disable()
            await add_source_window.populate_add_window(add_source_window)
        else:
            if data.Settings.valid_oauth==False:
                get_token()
    def delete_source(self, event):
        source_key=self.m_source_list.GetListView().GetItemText(self.m_source_list.GetListView().GetFocusedItem())
        if show_dialog("Are you sure you want to delete {}".format(source_key)):
            StartCoroutine(data.Sources.delete_source(source_key[source_key.find(" ")+1:]), self)
    async def add_userpage(self, links, scope):
        await data.Sources.add_user_source(links, scope)
    async def add_tournament(self, selection):
        await data.Sources.add_tournament_source(selection)
    async def add_osucollector(self, links):
        await data.Sources.add_osucollector_source(links)
    async def add_osuweblinks(self, title, links):
        await data.Sources.add_osuweblinks_source(title, links)

    async def create_osudb(self):
        self.m_add_source.Disable()
        self.m_toggle_downloading.Disable()
        self.m_save_settings.Disable()
        await database.create_osudb()
        # Refresh sources and jobs (the views will update)
        await data.Sources.refresh()
        self.m_add_source.Enable()
        self.m_toggle_downloading.Enable()
        self.m_save_settings.Enable()

        # Initiate automatic downloads
        if data.Settings.download_on_start:
            pub.sendMessage("toggle.jobs")
            StartCoroutine(self.toggle_jobs, self)
        
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
        self.Maximize(True)
        # bind the buttons to their respective callbacks
        AsyncBind(wx.EVT_BUTTON, self.add_userpage, self.m_add_userpage)
        AsyncBind(wx.EVT_BUTTON, self.add_tournament, self.m_add_tournament)
        AsyncBind(wx.EVT_BUTTON, self.add_mappack, self.m_add_mappack)
        AsyncBind(wx.EVT_BUTTON, self.add_osucollector, self.m_add_osucollector)
        AsyncBind(wx.EVT_BUTTON, self.add_osuweblinks, self.m_add_weblinks)
        AsyncBind(wx.EVT_CHOICE, self.change_mappack_section, self.m_mappack_section)
        AsyncBind(wx.EVT_WINDOW_DESTROY, self.onDestroy, self)

    async def onDestroy(self, event):
        global add_source_window
        global main_window
        add_source_window=None
        #User closed application
        if main_window != None:
            main_window.m_add_source.Enable()
            main_window.SetFocus()

    async def add_userpage(self, event):
        links=self.m_userpages.GetValue().strip()
        scope=[self.m_user_top100.GetValue(), self.m_user_favourites.GetValue(), self.m_user_everything.GetValue(),
                self.m_user_ranked.GetValue(), self.m_user_loved.GetValue(), self.m_user_pending.GetValue(), self.m_user_graveyarded.GetValue()]
        success=True
        if not "ppy.sh/users/" in links:
            show_dialog("You need to input a link to the osu user profile", focus_main=False)
            success=False
        if all(x==0 for x in scope):
            show_dialog("You need to select something to download from the userpage!", focus_main=False)
            success=False
        if success:
            self.Destroy()
            StartCoroutine(main_window.add_userpage(links, scope), main_window)
        
    async def add_tournament(self, event):
        selection=self.m_tournament.GetPageText(self.m_tournament.GetSelection())
        self.Destroy()
        StartCoroutine(main_window.add_tournament(selection), main_window)

    async def add_mappack(self, event):
        labels=[self.m_mappack_list.GetString(x) for x in self.m_mappack_list.GetSelections()]
        ids=[int(x.split(":")[0]) for x in labels]
        self.Destroy()
        await data.Sources.add_mappack_source(ids)

    async def add_osucollector(self, event):
        success=True
        links=self.m_osu_collector.GetValue().strip()
        if not "osucollector.com/collections/" in links:
            show_dialog("You need to input osucollector collection url", focus_main=False)
            success=False
        if success:
            self.Destroy()
            StartCoroutine(main_window.add_osucollector(links), main_window)

    async def add_osuweblinks(self, event):
        success=True
        title=self.m_osu_weblinks_key.GetValue().strip()
        links=self.m_osu_weblinks.GetValue().strip()
        if not title:
            show_dialog("You need to name the collection", focus_main=False)
            success=False
        if not "ppy.sh/beatmapsets/" in links:
            show_dialog("You need to input beatmaps for this collection", focus_main=False)
            success=False
        if success:
            self.Destroy()
            StartCoroutine(main_window.add_osuweblinks(title, links), main_window)

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
            add_tournament_panel=ListPanel(self.m_tournament)
            for beatmap in item[1][1]:
                beatmap_list.append(constants.osu_beatmap_url_full.format(beatmap[0], beatmap[2], beatmap[1]))
            tournament_key=item[0] + ": "+ item[1][0]
            if len(beatmap_list)>0:
                add_tournament_panel.m_list.InsertItems(beatmap_list,0)
            
            self.m_tournament.AddPage(add_tournament_panel, tournament_key)
            
            try:
                self.m_tournament.GetListView().SetColumnWidth(0,-1)
            except:
                pass
        
        mappack_list=[]
        for source_key, item in data.MappackJson["0"].items():
            source_name=item[0]
            mappack_list.append(f"{source_key}: {source_name} ({len(item[1])} beatmapsets)")
        if len(mappack_list)>0:
            self.m_mappack_list.InsertItems(mappack_list,0)
    def open_subscribed_mappers(self, event):
        webbrowser.open(constants.link_mappers)

class ListPanel(gui.ListPanel):
    def __init__(self, parent=None):
        super(ListPanel, self).__init__(parent)
        
    def open_beatmap_website(self, event):
        try:
            index = event.GetSelection()
            url=self.m_list.GetString(index).split()[0]
            webbrowser.open(url)
        except:
            pass

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
        selections=self.m_collections_selection.GetSelections()
        buen.generate_beatmaps(selections, self.current_collections)
        self.Destroy()
                
# Used for AddSourceWindow to call functions in main window
# There can be only one instance at all times
main_window = MainWindow()
add_source_window=None

async def main():
    main_window.SetIcon(wx.Icon(resource_path("osu.ico")))
    main_window.Show()
    app.SetTopWindow(main_window)
    has_savefile=await misc.init()
    
    if has_savefile==False:
        wizard=gui.IntroWizard(None)
        wizard.FitToPage(wizard.m_wizPage1)
        wizard.SetIcon(wx.Icon(resource_path("osu.ico")))
        wizard.m_oauth_btn.Bind(wx.EVT_BUTTON, get_oauth)
        wizard.RunWizard(wizard.m_wizPage1)
        data.Settings.osu_install_folder=wizard.m_osu_dir.GetPath()
    await main_window.restore_settings(None)
    await app.MainLoop()
asyncio.run(main())