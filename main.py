import wx
import gui
from Network import api, download, scraper
import Utilities as util
from wxasync import AsyncBind, WxAsyncApp
import asyncio
from asyncio.events import get_event_loop

class MainWindow(gui.Main):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)

	def show_add_window(self, event):
		add_source_window=gui.AddSource(parent=None)
		add_source_window.Show()
    #async def add_userpage(self, event):
    #    pass
        #provider.add_source(getdatafrominput)
	
async def main():            
    app = WxAsyncApp()
    frame = MainWindow()
    frame.Show()
    app.SetTopWindow(frame)
    await app.MainLoop()

asyncio.run(main())