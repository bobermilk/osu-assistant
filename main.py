from asyncio import coroutines
import wx
import gui
from wxasync import AsyncBind, WxAsyncApp
import asyncio
from Utilities import data, constants, misc
from pubsub import pub

app = WxAsyncApp()

# Used to allow updating of ui from outside using pub.sendMessage()
def update_sources():
    main_window.update_sources(None)

def update_activity():
    main_window.update_activity(None)

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
        AsyncBind(wx.EVT_BUTTON, self.toggle_jobs, self.m_toggle_downloading)

    # used to repopulate the source list after a edit
    def update_sources(self, event):
        self.m_activity_list.Clear()
        source_list=data.get_sources().read()
        for source_key, source in source_list:
            source_panel=gui.SourcePanel(self.m_source_list)
            for i, beatmapset_id, beatmap_id in enumerate(source.get_available_beatmaps()):
                source_panel.m_source.Insert(str(beatmap_id),i)
            for i, beatmapset_id, beatmap_id in enumerate(source.get_unavailable_beatmaps()):
                source_panel.m_source.Insert(str(beatmap_id)+" (unavailable)",i)
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
            data.cancel_jobs_toggle=True
            self.m_toggle_downloading.SetLabelText(constants.activity_start)
        elif not data.cancel_jobs_toggle:
            self.m_toggle_downloading.SetLabelText(constants.activity_stop)
            data.get_jobs().start_jobs()
            

    def show_add_window(self, event):
        add_source_window=AddSourceWindow(parent=None)
        add_source_window.Show()
        for i, source_key, tournament in enumerate(data.TournamentJson.items()):
            add_source_window.m_tournament_list.Insert(source_key + ": "+ tournament, i)
        # bind the buttons to their respective callbacks
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_userpage, add_source_window.m_add_userpage)
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_tournament, add_source_window.m_add_tournament)
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_mappack, add_source_window.m_add_mappack)
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_osucollector, add_source_window.m_add_osucollector)

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
                self.m_user_ranked.GetValue(), self.m_user_loved.GetValue(), self.m_user_guest_participation.GetValue(),
                self.m_user_pending.GetValue(), self.m_user_graveyarded.GetValue()]
        self.Destroy()
        data.get_sources().add_user_source(links, scope)
        main_window.update_sources(None)
        
    async def add_tournament(self, event):
        selection=self.m_tournament_list.GetString(self.m_tournament_list.GetSelection())
        self.Destroy()
        data.get_sources().add_tournament_source(selection)
        main_window.update_sources(None)

    async def add_mappack(self, event):
        ids=self.m_mappack_list.GetSelections()
        gamemode=self.m_mappack_gamemode.GetSelection()
        self.Destroy()
        data.get_sources().add_mappack_source(ids, gamemode)
        main_window.update_sources(None)

    async def add_osucollector(self, event):
        links=self.m_osu_collector.GetValue()
        self.Destroy()
        data.get_sources().add_osucollector_source(links)
        main_window.update_sources(None)

async def main():
    main_window.Show()
    app.SetTopWindow(main_window)
    app.MainLoop()

asyncio.run(main())
misc.init()