import wx
import gui
from wxasync import AsyncBind, WxAsyncApp
import asyncio
import Utilities.data as data
from asyncio.events import get_event_loop

class MainWindow(gui.Main):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    def show_add_window(self, event):
        add_source_window=AddSourceWindow(parent=None)
        add_source_window.Show()
        # bind the buttons to their respective callbacks
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_userpage, add_source_window.m_add_userpage)
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_tournament, add_source_window.m_add_tournament)
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_mappack, add_source_window.m_add_mappack)
        AsyncBind(wx.EVT_BUTTON, add_source_window.add_osucollector, add_source_window.m_add_osucollector)

class AddSourceWindow(gui.AddSource):
    def __init__(self, parent=None):
        super(AddSourceWindow, self).__init__(parent)
    
    async def add_userpage(self, event):
        links=self.m_userpages.GetValue()
        scope=[self.m_user_top100.GetValue(), self.m_user_favourites.GetValue(), self.m_user_everything.GetValue(),
                self.m_user_ranked.GetValue(), self.m_user_loved.GetValue(), self.m_user_guest_participation.GetValue(),
                self.m_user_pending.GetValue(), self.m_user_graveyarded.GetValue()]
        data.Sources.add_user_source(links, scope)
        
    async def add_tournament(self, event):
        selection=self.m_tournament_search.GetString(self.m_tournament_search.GetSelection())
        data.Sources.add_tournament_source(selection)

    async def add_mappack(self, event):
        status=self.m_mappack_status.GetSelection()
        gamemode=self.m_mappack_gamemode.GetSelection()
        download_count=self.m_mappack_beatmapcount.GetValue()
        data.Sources.add_mappack_source(status, gamemode, download_count)

    async def add_osucollector(self, event):
        links=self.m_osu_collector.GetValue()
        data.Sources.add_osucollector_source(links)

async def main():            
    app = WxAsyncApp()
    frame = MainWindow()
    frame.Show()
    app.SetTopWindow(frame)
    await app.MainLoop()

asyncio.run(main())