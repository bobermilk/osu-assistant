# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"osu! assistant", pos = wx.DefaultPosition, size = wx.Size( 1143,757 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_sources = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_source_list = wx.Listbook( self.m_panel_sources, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )

		bSizer4.Add( self.m_source_list, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_add_source = wx.Button( self.m_panel_sources, wx.ID_ANY, u"    Add source    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_add_source, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_sources.SetSizer( bSizer4 )
		self.m_panel_sources.Layout()
		bSizer4.Fit( self.m_panel_sources )
		self.m_notebook2.AddPage( self.m_panel_sources, u"Sources", False )
		self.m_panel_activity = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText23 = wx.StaticText( self.m_panel_activity, wx.ID_ANY, u"Download queue (drag to change download sequence)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer5.Add( self.m_staticText23, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		m_activity_listChoices = []
		self.m_activity_list = wx.ListBox( self.m_panel_activity, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_activity_listChoices, 0 )
		bSizer5.Add( self.m_activity_list, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_activity_progress = wx.StaticText( self.m_panel_activity, wx.ID_ANY, u"No active downloads!", wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE )
		self.m_activity_progress.Wrap( -1 )

		bSizer5.Add( self.m_activity_progress, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_progressbar = wx.Gauge( self.m_panel_activity, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_progressbar.SetValue( 0 )
		bSizer5.Add( self.m_progressbar, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_toggle_downloading = wx.Button( self.m_panel_activity, wx.ID_ANY, u"Start Downloading (top to bottom)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_toggle_downloading, 1, wx.ALL, 5 )


		bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )


		self.m_panel_activity.SetSizer( bSizer5 )
		self.m_panel_activity.Layout()
		bSizer5.Fit( self.m_panel_activity )
		self.m_notebook2.AddPage( self.m_panel_activity, u"Activity", False )
		self.m_panel_settings = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self.m_panel_settings, wx.ID_ANY, u"osu install folder:             \none directory above \nthe skins folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer26.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_osu_dir = wx.DirPickerCtrl( self.m_panel_settings, wx.ID_ANY, wx.EmptyString, u"Select your osu install folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer26.Add( self.m_osu_dir, 1, wx.ALL, 5 )


		bSizer25.Add( bSizer26, 0, wx.EXPAND, 5 )

		bSizer2611 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText412 = wx.StaticText( self.m_panel_settings, wx.ID_ANY, u"oauth app token:             \nused for osu api access", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText412.Wrap( -1 )

		bSizer2611.Add( self.m_staticText412, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_client_id = wx.TextCtrl( self.m_panel_settings, wx.ID_ANY, u"client_id", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2611.Add( self.m_client_id, 1, wx.ALL, 5 )

		self.m_client_secret = wx.TextCtrl( self.m_panel_settings, wx.ID_ANY, u"client_secret", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2611.Add( self.m_client_secret, 1, wx.ALL, 5 )


		bSizer25.Add( bSizer2611, 0, wx.EXPAND, 5 )

		self.m_autodownload_toggle = wx.CheckBox( self.m_panel_settings, wx.ID_ANY, u"Automatically start downloading from sources on application start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_autodownload_toggle, 0, wx.ALL, 5 )

		bSizer5511 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_export_to_collection = wx.Button( self.m_panel_settings, wx.ID_ANY, u"Export sources to database", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5511.Add( self.m_export_to_collection, 1, wx.ALL, 5 )

		self.m_export_to_beatmap = wx.Button( self.m_panel_settings, wx.ID_ANY, u"Export all in-game collections to beatmap", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5511.Add( self.m_export_to_beatmap, 1, wx.ALL, 5 )


		bSizer25.Add( bSizer5511, 0, wx.EXPAND, 5 )

		self.m_collapsiblePane1 = wx.CollapsiblePane( self.m_panel_settings, wx.ID_ANY, u"Advanced settings", wx.DefaultPosition, wx.DefaultSize, wx.CP_DEFAULT_STYLE )
		self.m_collapsiblePane1.Collapse( False )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"Unless you know what you're doing, leave these alone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer23.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_use_osu_mirror = wx.CheckBox( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"Use osu website as mirror if beatconnect does not have beatmap (botting is against TOS)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_use_osu_mirror, 0, wx.ALL, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer261 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"XSRF-TOKEN:    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer261.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_settings_xsrf_token = wx.TextCtrl( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer261.Add( self.m_settings_xsrf_token, 1, wx.ALL, 5 )


		bSizer34.Add( bSizer261, 1, 0, 5 )

		bSizer2612 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText413 = wx.StaticText( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"osu_session: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText413.Wrap( -1 )

		bSizer2612.Add( self.m_staticText413, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_settings_osu_session = wx.TextCtrl( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2612.Add( self.m_settings_osu_session, 1, wx.ALL, 5 )


		bSizer34.Add( bSizer2612, 1, 0, 5 )


		bSizer23.Add( bSizer34, 0, wx.EXPAND, 5 )

		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText411 = wx.StaticText( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"download interval (ms):    \ntoo low = rate limit\nrecommended: 1000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText411.Wrap( -1 )

		bSizer55.Add( self.m_staticText411, 0, wx.ALL, 5 )

		self.m_download_interval = wx.Slider( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, 1000, 0, 2000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer55.Add( self.m_download_interval, 1, wx.ALL, 5 )


		bSizer23.Add( bSizer55, 0, wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"Restore all settings to defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_button13, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer551 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_import_assistant = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"Import osu!assistant configuration", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer551.Add( self.m_import_assistant, 1, wx.ALL, 5 )

		self.m_export_assistant = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"Export osu! assistant configuration", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer551.Add( self.m_export_assistant, 1, wx.ALL, 5 )


		bSizer23.Add( bSizer551, 1, wx.EXPAND, 5 )


		self.m_collapsiblePane1.GetPane().SetSizer( bSizer23 )
		self.m_collapsiblePane1.GetPane().Layout()
		bSizer23.Fit( self.m_collapsiblePane1.GetPane() )
		bSizer25.Add( self.m_collapsiblePane1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_save_settings = wx.Button( self.m_panel_settings, wx.ID_ANY, u"Save settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_save_settings, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_settings.SetSizer( bSizer25 )
		self.m_panel_settings.Layout()
		bSizer25.Fit( self.m_panel_settings )
		self.m_notebook2.AddPage( self.m_panel_settings, u"Settings", False )
		self.m_panel_help = wx.ScrolledWindow( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_panel_help.SetScrollRate( 5, 5 )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		bSizer281 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_website = wx.Button( self.m_panel_help, wx.ID_ANY, u"Wiki", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.m_website, 0, wx.ALL, 5 )

		self.m_discord = wx.Button( self.m_panel_help, wx.ID_ANY, u"Discord", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.m_discord, 0, wx.ALL, 5 )

		self.m_github = wx.Button( self.m_panel_help, wx.ID_ANY, u"Github", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.m_github, 0, wx.ALL, 5 )

		self.m_donate = wx.Button( self.m_panel_help, wx.ID_ANY, u"Donate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.m_donate, 0, wx.ALL, 5 )


		bSizer24.Add( bSizer281, 1, 0, 5 )

		self.m_instructions = wx.StaticText( self.m_panel_help, wx.ID_ANY, u"osu! assistant allows you to watch beatmap sources and download and keep them updated without you having to do it manually.\n\nFollow instruction 1, 2 and 3 below and you should be able to get the beatmaps you want, completely free of charge. The instructions follow the format below.\n\n0. Example step\n    --> Tab (information about this tab)\n        - thing 1 to do in this tab\n        - thing 2 to do in this tab\n\nInstructions:\n\n1. Configuration\n    --> Settings (configurations stuff are here)\n        - set your osu installation folder\n        - set your client id and secret (osu settings -> New OAuth Application -> fill up with anything  and click register)\n        - Optional: enable download from osu, get XSRF-TOKEN and osu_session by inspect element -> network -> reload osu page ->\n                          find the entry with set-cookies -> you want everything between = and ;\n        - click save settings\n\n2. Telling osu! assistant where to get beatmaps:\n    --> Sources\n        - Click add a new source button (choose from the following)\n        --> Userpage (beatmaps from a osu player/mapper userpage):\n            - Paste the url of profiles you would like to download from\n            - Select user favourites/top plays\n            - Select mapper ranked/loved/guest participation/pending/graveyarded\n    \n         --> Tournament (beatmaps from tournament mappool):\n            - Specify game mode of tournament and whether it's official or unofficial\n            - Check the tournaments you want\n    \n          --> Mappacks (latest beatmaps from various sources)\n            - Specify the game mode and category of beatmaps you want \n            - Specify the number of latest beatmaps you want\n    \n          --> osu!Collector (beatmaps from osucollector.com)\n            - Paste the urls of osu!Collector collection pages, leave a new line or space after each link\n\n        - click add button\n\n3. Downloading the beatmaps you told osu assistant to get:\n    --> Activity (shows the download queue)\n        - Look at the job list. If you are satisfied, press start downloads.\n        - Start the download and wait until the progress bar reaches 100%\n        - Open the game and see your beatmaps import, and the source collection should be merged with your existing collections.db\n\n    --> Sources (shows the sources you added)\n        - Update ongoing changes from your sources here\n          (example: ongoing tournament released new beatmaps, i add them by clicking update in the dashboard app)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_instructions.Wrap( -1 )

		self.m_instructions.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.m_instructions, 0, wx.ALL, 5 )


		self.m_panel_help.SetSizer( bSizer24 )
		self.m_panel_help.Layout()
		bSizer24.Fit( self.m_panel_help )
		self.m_notebook2.AddPage( self.m_panel_help, u"Help", True )

		bSizer1.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_osu_dir.Bind( wx.EVT_DIRPICKER_CHANGED, self.update_osu_folder )
		self.m_autodownload_toggle.Bind( wx.EVT_CHECKBOX, self.autodownload_toggle )
		self.m_export_to_collection.Bind( wx.EVT_BUTTON, self.import_assistant_configuration )
		self.m_export_to_beatmap.Bind( wx.EVT_BUTTON, self.export_assistant_configuration )
		self.m_import_assistant.Bind( wx.EVT_BUTTON, self.import_assistant_configuration )
		self.m_export_assistant.Bind( wx.EVT_BUTTON, self.export_assistant_configuration )
		self.m_save_settings.Bind( wx.EVT_BUTTON, self.save_settings )
		self.m_website.Bind( wx.EVT_BUTTON, self.open_website )
		self.m_discord.Bind( wx.EVT_BUTTON, self.open_discord )
		self.m_github.Bind( wx.EVT_BUTTON, self.open_github )
		self.m_donate.Bind( wx.EVT_BUTTON, self.open_donate )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def update_osu_folder( self, event ):
		event.Skip()

	def autodownload_toggle( self, event ):
		event.Skip()

	def import_assistant_configuration( self, event ):
		event.Skip()

	def export_assistant_configuration( self, event ):
		event.Skip()



	def save_settings( self, event ):
		event.Skip()

	def open_website( self, event ):
		event.Skip()

	def open_discord( self, event ):
		event.Skip()

	def open_github( self, event ):
		event.Skip()

	def open_donate( self, event ):
		event.Skip()


###########################################################################
## Class AddSource
###########################################################################

class AddSource ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add source", pos = wx.DefaultPosition, size = wx.Size( 768,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel6 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Links of userpage links (add new line or space after a link)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer35.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_subscribed_mappers = wx.Button( self.m_panel6, wx.ID_ANY, u"        Get subscribed mappers        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.m_subscribed_mappers, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )


		bSizer7.Add( bSizer35, 0, wx.EXPAND, 5 )

		self.m_userpages = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_MULTILINE )
		self.m_userpages.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer7.Add( self.m_userpages, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_user_top100 = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Top 100 plays (specify gamemode in url)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_user_top100, 0, wx.ALL, 5 )

		self.m_user_favourites = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Favourites", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_user_favourites, 0, wx.ALL, 5 )

		self.m_user_everything = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"All beatmaps ever played", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_user_everything, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer10, 0, wx.EXPAND, 5 )

		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_user_ranked = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Ranked", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_user_ranked, 0, wx.ALL, 5 )

		self.m_user_loved = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Loved", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_user_loved, 0, wx.ALL, 5 )

		self.m_user_pending = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Pending", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_user_pending, 0, wx.ALL, 5 )

		self.m_user_graveyarded = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Graveyarded", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_user_graveyarded, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer101, 0, wx.EXPAND, 5 )

		self.m_add_userpage = wx.Button( self.m_panel6, wx.ID_ANY, u"Add Userpage(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_add_userpage, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel6.SetSizer( bSizer7 )
		self.m_panel6.Layout()
		bSizer7.Fit( self.m_panel6 )
		self.m_notebook2.AddPage( self.m_panel6, u"Userpage", True )
		self.m_panel7 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_tournament = wx.Listbook( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )

		bSizer14.Add( self.m_tournament, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_add_tournament = wx.Button( self.m_panel7, wx.ID_ANY, u"Add Tournament", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_add_tournament, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		self.m_notebook2.AddPage( self.m_panel7, u"Tournament", False )
		self.m_panel8 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer141 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText41231 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Mappack section", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41231.Wrap( -1 )

		bSizer141.Add( self.m_staticText41231, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		m_mappack_sectionChoices = [ u"Standard", u"Spotlight", u"Theme", u"Artist/Album" ]
		self.m_mappack_section = wx.Choice( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_mappack_sectionChoices, 0 )
		self.m_mappack_section.SetSelection( 0 )
		bSizer141.Add( self.m_mappack_section, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Search results", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer141.Add( self.m_staticText17, 0, wx.ALL, 5 )

		m_mappack_listChoices = []
		self.m_mappack_list = wx.ListBox( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_mappack_listChoices, wx.LB_MULTIPLE )
		bSizer141.Add( self.m_mappack_list, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_add_mappack = wx.Button( self.m_panel8, wx.ID_ANY, u"Add Mappack(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_add_mappack, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel8.SetSizer( bSizer141 )
		self.m_panel8.Layout()
		bSizer141.Fit( self.m_panel8 )
		self.m_notebook2.AddPage( self.m_panel8, u"Mappacks", False )
		self.m_panel9 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer241 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Links of osu collector links (add new line or space after a link)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer241.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_osu_collector = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_MULTILINE )
		self.m_osu_collector.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer241.Add( self.m_osu_collector, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_add_osucollector = wx.Button( self.m_panel9, wx.ID_ANY, u"Add Collection(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.m_add_osucollector, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel9.SetSizer( bSizer241 )
		self.m_panel9.Layout()
		bSizer241.Fit( self.m_panel9 )
		self.m_notebook2.AddPage( self.m_panel9, u"osu!Collector", False )

		bSizer1.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_subscribed_mappers.Bind( wx.EVT_BUTTON, self.open_subscribed_mappers )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def open_subscribed_mappers( self, event ):
		event.Skip()


###########################################################################
## Class ListPanel
###########################################################################

class ListPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		m_listChoices = []
		self.m_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listChoices, 0 )
		bSizer31.Add( self.m_list, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer31 )
		self.Layout()

	def __del__( self ):
		pass


