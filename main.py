from asyncio import coroutines
import wx
import gui
from wxasync import AsyncBind, WxAsyncApp
import asyncio
import data, constants, misc
from pubsub import pub

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
    main_window.m_toggle_downloading.Enable()

class MainWindow(gui.Main):
    """
    Main window bro
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.update_sources(self)
        self.update_activity(self)
        pub.subscribe(update_sources, "update.sources")
        pub.subscribe(update_activity, "update.activity")
        pub.subscribe(update_progress, "update.progress")
        pub.subscribe(update_progress, "update.progress")
        pub.subscribe(enable_job_toggle_button, "enable.job_toggle_button")
        AsyncBind(wx.EVT_BUTTON, self.show_add_window, self.m_add_source)
        AsyncBind(wx.EVT_BUTTON, self.toggle_jobs, self.m_toggle_downloading)

    # used to repopulate the source list after a edit
    def update_sources(self, event):
        self.m_source_list.DeleteAllPages()
        source_list=data.get_sources().read()
        for source_key, source in source_list:
            source_panel=gui.ListPanel(self.m_source_list)
            for i, beatmap in enumerate(source.get_available_beatmaps()):
                source_panel.m_list.Insert("beatmapset_id="+str(beatmap[0]) + " beatmap_id="+str(beatmap[1]),i)
            for i, beatmap in enumerate(source.get_unavailable_beatmaps()):
                source_panel.m_list.Insert("beatmapset_id="+str(beatmap[0]) + " beatmap_id="+str(beatmap[1] + " (unavailable for download)"),i)
            for i, beatmap in enumerate(source.get_missing_beatmaps()):
                source_panel.m_list.Insert("beatmapset_id="+str(beatmap[0]) + " beatmap_id="+str(beatmap[1] + " (missing)"),i)
            self.m_source_list.AddPage(source_panel, source_key)

    # used to repopulate the activity list after download completes
    def update_activity(self, event):
        self.m_activity_list.Clear()
        job_list=data.get_jobs().read()
        i=0
        while len(job_list) > 0:
            job=job_list.pop(0)
            job_source_key=job.get_job_source_key()
            self.m_activity_list.Insert(str(job_source_key+f" ({job.get_job_downloads_cnt()} beatmaps)"), i)

    # toggle jobs
    # TODO: 
    async def toggle_jobs(self, event):
        self.m_toggle_downloading.Disable()
        if self.m_toggle_downloading.GetLabel() == constants.activity_stop:
            data.cancel_jobs_toggle=True
            self.m_toggle_downloading.SetLabelText(constants.activity_start)
        elif not data.cancel_jobs_toggle:
            self.m_toggle_downloading.SetLabelText(constants.activity_stop)
            await data.get_jobs().start_jobs()

    async def show_add_window(self, event):
        global add_source_window
        add_source_window=AddSourceWindow(parent=None)
        add_source_window.Show()
        self.m_add_source.Disable()
        await add_source_window.populate_add_window(add_source_window)

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

# Used for AddSourceWindow to call functions in main window
# There can be only one instance at all times
main_window = MainWindow()
add_source_window=None

async def main():
    main_window.Show()
    app.SetTopWindow(main_window)
    await misc.init()
    await app.MainLoop()

asyncio.run(main())