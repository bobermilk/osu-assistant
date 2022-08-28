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
                source_panel.m_list.Insert("beatmapset_id="+str(beatmap[0]) + " beatmap_id="+str(beatmap[1]),i)
            self.m_source_list.AddPage(source_panel, source_key)

    # used to repopulate the activity list after download completes
    def update_activity(self, event):
        self.m_activity_list.Clear()
        job_list=data.get_jobs().read()
        i=0
        while len(job_list) > 0:
            job=job_list.pop(0)
            job_source_key=job.get_job_source_key()
            job_status=job.get_status()
            self.m_activity_list.Insert(str(job_source_key+f" ({job_status})"), i)

    # toggle jobs
    # TODO: 
    async def toggle_jobs(self, event):
        if self.m_toggle_downloading.GetLabel() == constants.activity_stop:
            if len(data.get_jobs().job_queue)>0:
                data.cancel_jobs_toggle=True
                self.m_toggle_downloading.SetLabelText(constants.activity_start)
            else:
                self.m_toggle_downloading.SetLabelText(constants.activity_start)
        elif not data.cancel_jobs_toggle:
            self.m_toggle_downloading.SetLabelText(constants.activity_stop)
            await data.get_jobs().start_jobs()

    async def show_add_window(self, event):
        add_source_window=AddSourceWindow(parent=None)
        for item in data.TournamentJson.items():
            add_tournament_panel=gui.ListPanel(add_source_window.m_tournament)
            for j, beatmap in enumerate(item[1][1]):
                add_tournament_panel.m_list.Insert(constants.osu_beatmap_url_full.format(beatmap[0], beatmap[2], beatmap[1]), j)
            tournament_key=item[0] + ": "+ item[1][0]
            
            add_source_window.m_tournament.AddPage(add_tournament_panel, tournament_key)

        for i, item in enumerate(data.MappackJson["0"].items()):
            add_source_window.m_mappack_list.Insert(str(item[0] + f" ({len(item[1])} beatmapsets)"), i)
        add_source_window.Show()
        # bind the buttons to their respective callbacks
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_userpage, add_source_window.m_add_userpage)
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_tournament, add_source_window.m_add_tournament)
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_mappack, add_source_window.m_add_mappack)
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_osucollector, add_source_window.m_add_osucollector)
        AsyncBind(wx.EVT_CHOICE, add_source_window.change_mappack_section, add_source_window.m_mappack_section)
        

# Used for AddSourceWindow to call functions in main window
# There can be only one instance at all times
main_window = MainWindow()

class AddSourceWindow(gui.AddSource):
    """
    Window for adding a new source
    """
    def __init__(self, parent=None):
        super(AddSourceWindow, self).__init__(parent)
    
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
        ids=self.m_mappack_list.GetSelections()
        self.Destroy()
        await data.get_sources().add_mappack_source(ids)

    async def add_osucollector(self, event):
        links=self.m_osu_collector.GetValue()
        self.Destroy()
        await data.get_sources().add_osucollector_source(links)

    async def change_mappack_section(self, event):
        selection=str(self.m_mappack_section.GetSelection())
        self.m_mappack_list.Clear()
        for i, item in enumerate(data.MappackJson[selection].items()):
            self.m_mappack_list.Insert(str(item[0] + f" ({len(item[1])} beatmapsets)"), i)

async def main():
    main_window.Show()
    app.SetTopWindow(main_window)
    await misc.init()
    await app.MainLoop()

asyncio.run(main())