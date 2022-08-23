import wx
import gui
from wxasync import AsyncBind, WxAsyncApp
import asyncio
import Utilities.data as data
from asyncio.events import get_event_loop
    
app = WxAsyncApp()

class MainWindow(gui.Main):
    """
    Main window bro
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.update_sources(self)

    # used to repopulate the source list after a edit
    def update_sources(self, event):
        # TODO: clear source list
        source_list=data.get_sources_list()
        for source_key, source in source_list:
            source_panel=gui.SourcePanel(self.m_source_list)
            for i, map in enumerate(source.get_all_beatmaps()):
                source_panel.m_source.Insert(str(map),i)
            for i, map in enumerate(source.get_unavailable_beatmaps()):
                source_panel.m_source.Insert(str(map)+" (unavailable)",i)
            self.m_source_list.AddPage(source_panel, source_key)

    def show_add_window(self, event):
        add_source_window=AddSourceWindow(parent=None)
        add_source_window.Show()
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
        data.Sources.add_user_source(links, scope)
        main_window.update_sources(None)
        
    async def add_tournament(self, event):
        selection=self.m_tournament_search.GetString(self.m_tournament_search.GetSelection())
        self.Destroy()
        data.Sources.add_tournament_source(selection)
        main_window.update_sources(None)

    async def add_mappack(self, event):
        status=self.m_mappack_status.GetSelection()
        gamemode=self.m_mappack_gamemode.GetSelection()
        download_count=self.m_mappack_beatmapcount.GetValue()
        self.Destroy()
        data.Sources.add_mappack_source(status, gamemode, download_count)
        main_window.update_sources(None)

    async def add_osucollector(self, event):
        links=self.m_osu_collector.GetValue()
        self.Destroy()
        data.Sources.add_osucollector_source(links)
        main_window.update_sources(None)

async def main():
    main_window.Show()
    app.SetTopWindow(main_window)
    await app.MainLoop()

asyncio.run(main())