# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"osu! assistant", pos = wx.DefaultPosition, size = wx.Size( 1143,757 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_tabs = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_tabs.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		self.m_panel_sources = wx.Panel( self.m_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_source_list = wx.Listbook( self.m_panel_sources, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_source_list.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )


		bSizer4.Add( self.m_source_list, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_add_source = wx.Button( self.m_panel_sources, wx.ID_ANY, u"    Add source    ", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_add_source.SetFont( wx.Font( 21, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer241.Add( self.m_add_source, 1, wx.ALL, 5 )


		bSizer4.Add( bSizer241, 0, wx.EXPAND, 5 )


		self.m_panel_sources.SetSizer( bSizer4 )
		self.m_panel_sources.Layout()
		bSizer4.Fit( self.m_panel_sources )
		self.m_tabs.AddPage( self.m_panel_sources, u"Sources", True )
		self.m_panel_activity = wx.Panel( self.m_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		activity_box = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText23 = wx.StaticText( self.m_panel_activity, wx.ID_ANY, u"Download queue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		self.m_staticText23.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		activity_box.Add( self.m_staticText23, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		m_activity_listChoices = []
		self.m_activity_list = wx.ListBox( self.m_panel_activity, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_activity_listChoices, 0 )
		activity_box.Add( self.m_activity_list, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_activity_progress = wx.StaticText( self.m_panel_activity, wx.ID_ANY, u"No active downloads!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_activity_progress.Wrap( -1 )

		self.m_activity_progress.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		activity_box.Add( self.m_activity_progress, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_progressbar = wx.Gauge( self.m_panel_activity, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,30 ), wx.GA_HORIZONTAL )
		self.m_progressbar.SetValue( 0 )
		activity_box.Add( self.m_progressbar, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_toggle_downloading = wx.Button( self.m_panel_activity, wx.ID_ANY, u"Start Downloading", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_toggle_downloading.SetFont( wx.Font( 21, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.m_toggle_downloading, 1, wx.ALL, 5 )


		activity_box.Add( bSizer6, 0, wx.EXPAND, 5 )


		self.m_panel_activity.SetSizer( activity_box )
		self.m_panel_activity.Layout()
		activity_box.Fit( self.m_panel_activity )
		self.m_tabs.AddPage( self.m_panel_activity, u"Activity", False )
		self.m_panel_settings = wx.Panel( self.m_tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self.m_panel_settings, wx.ID_ANY, u"osu install folder:\n(example: C:\\Users\\foo\\AppData\\Local\\osu!)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_osu_dir = wx.DirPickerCtrl( self.m_panel_settings, wx.ID_ANY, wx.EmptyString, u"Select your osu install folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_osu_dir.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26.Add( self.m_osu_dir, 1, wx.ALL, 5 )


		bSizer25.Add( bSizer26, 0, wx.EXPAND, 5 )

		self.m_autodownload_toggle = wx.CheckBox( self.m_panel_settings, wx.ID_ANY, u"Automatically start downloading from sources on application start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_autodownload_toggle.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer25.Add( self.m_autodownload_toggle, 0, wx.ALL, 5 )

		bSizer5511 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer25.Add( bSizer5511, 0, wx.EXPAND, 5 )

		self.m_collapsiblePane1 = wx.CollapsiblePane( self.m_panel_settings, wx.ID_ANY, u"Advanced settings", wx.DefaultPosition, wx.DefaultSize, wx.CP_DEFAULT_STYLE )
		self.m_collapsiblePane1.Collapse( False )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"Unless you know what you're doing, leave these alone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer23.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_use_osu_mirror = wx.CheckBox( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"Use osu website as mirror if chimu does not have beatmap (botting is against the osu terms of service, but there should be no issue with using this)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_use_osu_mirror.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer23.Add( self.m_use_osu_mirror, 0, wx.ALL, 5 )

		bSizer26111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4121 = wx.StaticText( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"if option above is checked:      \nobtain and fill (read help panel)\nXSRF_TOKEN and osu_session", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4121.Wrap( -1 )

		self.m_staticText4121.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26111.Add( self.m_staticText4121, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_settings_xsrf_token = wx.TextCtrl( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"XSRF_TOKEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_settings_xsrf_token.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26111.Add( self.m_settings_xsrf_token, 1, wx.ALL, 5 )

		self.m_settings_osu_session = wx.TextCtrl( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"osu_session", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_settings_osu_session.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26111.Add( self.m_settings_osu_session, 1, wx.ALL, 5 )


		bSizer23.Add( bSizer26111, 0, wx.EXPAND, 5 )

		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText411 = wx.StaticText( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"download interval (ms):    \ntoo low = rate limit\nrecommended: 1000", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText411.Wrap( -1 )

		self.m_staticText411.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer55.Add( self.m_staticText411, 0, wx.ALL, 5 )

		self.m_download_interval = wx.Slider( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, 1000, 0, 2000, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		bSizer55.Add( self.m_download_interval, 1, wx.ALL, 5 )


		bSizer23.Add( bSizer55, 0, wx.EXPAND, 5 )

		self.m_export_to_beatmap = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, u"Convert a in-game collection to beatmap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_export_to_beatmap.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer23.Add( self.m_export_to_beatmap, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_collapsiblePane1.GetPane().SetSizer( bSizer23 )
		self.m_collapsiblePane1.GetPane().Layout()
		bSizer23.Fit( self.m_collapsiblePane1.GetPane() )
		bSizer25.Add( self.m_collapsiblePane1, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		bSizer281 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_website = wx.Button( self.m_panel_settings, wx.ID_ANY, u"Wiki", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_website.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer281.Add( self.m_website, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_discord = wx.Button( self.m_panel_settings, wx.ID_ANY, u"Discord", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_discord.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer281.Add( self.m_discord, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_github = wx.Button( self.m_panel_settings, wx.ID_ANY, u"Github", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_github.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer281.Add( self.m_github, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_donate = wx.Button( self.m_panel_settings, wx.ID_ANY, u"Donate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_donate.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer281.Add( self.m_donate, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer24.Add( bSizer281, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_version = wx.StaticText( self.m_panel_settings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_version.Wrap( -1 )

		bSizer24.Add( self.m_version, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer25.Add( bSizer24, 1, wx.EXPAND, 5 )

		self.m_save_settings = wx.Button( self.m_panel_settings, wx.ID_ANY, u"Save settings", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_save_settings.SetFont( wx.Font( 21, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer25.Add( self.m_save_settings, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_settings.SetSizer( bSizer25 )
		self.m_panel_settings.Layout()
		bSizer25.Fit( self.m_panel_settings )
		self.m_tabs.AddPage( self.m_panel_settings, u"Settings", False )

		bSizer1.Add( self.m_tabs, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_osu_dir.Bind( wx.EVT_DIRPICKER_CHANGED, self.update_osu_folder )
		self.m_autodownload_toggle.Bind( wx.EVT_CHECKBOX, self.autodownload_toggle )
		self.m_export_to_beatmap.Bind( wx.EVT_BUTTON, self.export_collection_to_beatmap )
		self.m_website.Bind( wx.EVT_BUTTON, self.open_website )
		self.m_discord.Bind( wx.EVT_BUTTON, self.open_discord )
		self.m_github.Bind( wx.EVT_BUTTON, self.open_github )
		self.m_donate.Bind( wx.EVT_BUTTON, self.open_donate )
		self.m_save_settings.Bind( wx.EVT_BUTTON, self.save_settings )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def update_osu_folder( self, event ):
		event.Skip()

	def autodownload_toggle( self, event ):
		event.Skip()

	def export_collection_to_beatmap( self, event ):
		event.Skip()

	def open_website( self, event ):
		event.Skip()

	def open_discord( self, event ):
		event.Skip()

	def open_github( self, event ):
		event.Skip()

	def open_donate( self, event ):
		event.Skip()

	def save_settings( self, event ):
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

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer35.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_subscribed_mappers = wx.Button( self.m_panel6, wx.ID_ANY, u"        Get subscribed mappers        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_subscribed_mappers.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer35.Add( self.m_subscribed_mappers, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )


		bSizer7.Add( bSizer35, 0, wx.EXPAND, 5 )

		self.m_userpages = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_MULTILINE )
		self.m_userpages.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer7.Add( self.m_userpages, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_user_top100 = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Top 100 plays (specify gamemode in url)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_user_top100.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer10.Add( self.m_user_top100, 0, wx.ALL, 5 )

		self.m_user_favourites = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Favourites", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_user_favourites.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer10.Add( self.m_user_favourites, 0, wx.ALL, 5 )

		self.m_user_everything = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"All beatmaps ever played", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_user_everything.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer10.Add( self.m_user_everything, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer10, 0, wx.EXPAND, 5 )

		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_user_ranked = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Ranked", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_user_ranked.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer101.Add( self.m_user_ranked, 0, wx.ALL, 5 )

		self.m_user_loved = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Loved", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_user_loved.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer101.Add( self.m_user_loved, 0, wx.ALL, 5 )

		self.m_user_pending = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Pending", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_user_pending.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer101.Add( self.m_user_pending, 0, wx.ALL, 5 )

		self.m_user_graveyarded = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Graveyarded", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_user_graveyarded.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer101.Add( self.m_user_graveyarded, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer101, 0, wx.EXPAND, 5 )

		self.m_add_userpage = wx.Button( self.m_panel6, wx.ID_ANY, u"Add Userpage(s)", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_add_userpage.SetFont( wx.Font( 21, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer7.Add( self.m_add_userpage, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel6.SetSizer( bSizer7 )
		self.m_panel6.Layout()
		bSizer7.Fit( self.m_panel6 )
		self.m_notebook2.AddPage( self.m_panel6, u"Userpage", True )
		self.m_panel7 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_tournament = wx.Listbook( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_tournament.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )


		bSizer14.Add( self.m_tournament, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_add_tournament = wx.Button( self.m_panel7, wx.ID_ANY, u"Add Tournament", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_add_tournament.SetFont( wx.Font( 21, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer14.Add( self.m_add_tournament, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		self.m_notebook2.AddPage( self.m_panel7, u"Tournament", False )
		self.m_panel8 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer141 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText41231 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Mappack section", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41231.Wrap( -1 )

		self.m_staticText41231.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer141.Add( self.m_staticText41231, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		m_mappack_sectionChoices = [ u"Standard", u"Spotlight", u"Theme", u"Artist/Album" ]
		self.m_mappack_section = wx.Choice( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_mappack_sectionChoices, 0 )
		self.m_mappack_section.SetSelection( 0 )
		self.m_mappack_section.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer141.Add( self.m_mappack_section, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Search results (hold control and click to select multiple packs)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer141.Add( self.m_staticText17, 0, wx.ALL, 5 )

		m_mappack_listChoices = []
		self.m_mappack_list = wx.ListBox( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_mappack_listChoices, wx.LB_MULTIPLE )
		self.m_mappack_list.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer141.Add( self.m_mappack_list, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_add_mappack = wx.Button( self.m_panel8, wx.ID_ANY, u"Add Mappack(s)", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_add_mappack.SetFont( wx.Font( 21, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer141.Add( self.m_add_mappack, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel8.SetSizer( bSizer141 )
		self.m_panel8.Layout()
		bSizer141.Fit( self.m_panel8 )
		self.m_notebook2.AddPage( self.m_panel8, u"Mappacks", False )
		self.m_panel9 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer241 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Links of osu collector links (add new line or space after a link)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer241.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_osu_collector = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_MULTILINE )
		self.m_osu_collector.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer241.Add( self.m_osu_collector, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_add_osucollector = wx.Button( self.m_panel9, wx.ID_ANY, u"Add Collection(s)", wx.DefaultPosition, wx.Size( -1,60 ), 0 )
		self.m_add_osucollector.SetFont( wx.Font( 21, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

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


###########################################################################
## Class CollectionsSelection
###########################################################################

class CollectionsSelection ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select collections to export to beatmap", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		m_collections_selectionChoices = []
		self.m_collections_selection = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_collections_selectionChoices, wx.LB_MULTIPLE )
		bSizer24.Add( self.m_collections_selection, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_collections_select_btn = wx.Button( self, wx.ID_ANY, u"Export selected collection(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_collections_select_btn, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer24 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_collections_select_btn.Bind( wx.EVT_BUTTON, self.export_collections_to_beatmap )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def export_collections_to_beatmap( self, event ):
		event.Skip()


###########################################################################
## Class IntroWizard
###########################################################################

class IntroWizard ( wx.adv.Wizard ):

	def __init__( self, parent ):
		wx.adv.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, bitmap = wx.NullBitmap, pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.m_pages = []

		self.m_wizPage1 = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_wizPage1 )

		bSizer261 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText181 = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"Welcome to osu! assistant", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		self.m_staticText181.SetFont( wx.Font( 24, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )
		self.m_staticText181.SetMinSize( wx.Size( -1,50 ) )

		bSizer261.Add( self.m_staticText181, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_wizPage1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer261.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText191 = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"Features:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )

		self.m_staticText191.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText191.SetMinSize( wx.Size( -1,30 ) )

		bSizer261.Add( self.m_staticText191, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText161 = wx.StaticText( self.m_wizPage1, wx.ID_ANY, u"• Bulk downloading from beatmap sources\n• Writing downloaded beatmaps to in-game collections\n• Beatmap sources allow future updates to be synced automatically\n• No loading screens so whenever the app is loading it just hangs", wx.DefaultPosition, wx.Size( 1000,400 ), 0 )
		self.m_staticText161.Wrap( -1 )

		self.m_staticText161.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer261.Add( self.m_staticText161, 0, wx.ALL, 5 )


		self.m_wizPage1.SetSizer( bSizer261 )
		self.m_wizPage1.Layout()
		bSizer261.Fit( self.m_wizPage1 )
		self.m_wizPage2 = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_wizPage2 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText18 = wx.StaticText( self.m_wizPage2, wx.ID_ANY, u"Beatmap Sources", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( 24, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )
		self.m_staticText18.SetMinSize( wx.Size( -1,50 ) )

		bSizer26.Add( self.m_staticText18, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_wizPage2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer26.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.m_wizPage2, wx.ID_ANY, u"osu! assistant adds beatmaps from:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText19.SetMinSize( wx.Size( -1,30 ) )

		bSizer26.Add( self.m_staticText19, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText16 = wx.StaticText( self.m_wizPage2, wx.ID_ANY, u"• userpages on the osu website\n• tournaments\n• mappacks\n• osu!Collector collection link\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26.Add( self.m_staticText16, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_wizPage2.SetSizer( bSizer26 )
		self.m_wizPage2.Layout()
		bSizer26.Fit( self.m_wizPage2 )
		self.m_wizPage3 = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_wizPage3 )

		bSizer262 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText182 = wx.StaticText( self.m_wizPage3, wx.ID_ANY, u"How to use?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText182.Wrap( -1 )

		self.m_staticText182.SetFont( wx.Font( 24, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )
		self.m_staticText182.SetMinSize( wx.Size( -1,50 ) )

		bSizer262.Add( self.m_staticText182, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self.m_wizPage3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer262.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText192 = wx.StaticText( self.m_wizPage3, wx.ID_ANY, u"very ez:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText192.Wrap( -1 )

		self.m_staticText192.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText192.SetMinSize( wx.Size( -1,30 ) )

		bSizer262.Add( self.m_staticText192, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText162 = wx.StaticText( self.m_wizPage3, wx.ID_ANY, u"1. Close osu!\n2. Add as many beatmaps sources as you want\n3. Start downloads \n4. Open osu! to see new collections", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )

		self.m_staticText162.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer262.Add( self.m_staticText162, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_wizPage3.SetSizer( bSizer262 )
		self.m_wizPage3.Layout()
		bSizer262.Fit( self.m_wizPage3 )
		self.m_wizPage4 = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_wizPage4 )

		bSizer2621 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1821 = wx.StaticText( self.m_wizPage4, wx.ID_ANY, u"Before we begin...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1821.Wrap( -1 )

		self.m_staticText1821.SetFont( wx.Font( 24, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Comic Sans MS" ) )
		self.m_staticText1821.SetMinSize( wx.Size( -1,50 ) )

		bSizer2621.Add( self.m_staticText1821, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self.m_wizPage4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2621.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText1921 = wx.StaticText( self.m_wizPage4, wx.ID_ANY, u"osu! assistant needs 2 things:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1921.Wrap( -1 )

		self.m_staticText1921.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_staticText1921.SetMinSize( wx.Size( -1,30 ) )

		bSizer2621.Add( self.m_staticText1921, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer263 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText25 = wx.StaticText( self.m_wizPage4, wx.ID_ANY, u"1. osu install folder:\n(example: C:\\Users\\foo\\AppData\\Local\\osu!)", wx.DefaultPosition, wx.Size( 250,100 ), 0 )
		self.m_staticText25.Wrap( -1 )

		self.m_staticText25.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer263.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_osu_dir = wx.DirPickerCtrl( self.m_wizPage4, wx.ID_ANY, wx.EmptyString, u"Select your osu install folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_osu_dir.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer263.Add( self.m_osu_dir, 1, wx.ALL, 5 )


		bSizer2621.Add( bSizer263, 0, wx.EXPAND, 5 )

		bSizer2611 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_oauth_btn = wx.Button( self.m_wizPage4, wx.ID_ANY, u"2. Grant assistant access to the osu! api", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_oauth_btn.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer2611.Add( self.m_oauth_btn, 1, wx.ALL, 5 )


		bSizer2621.Add( bSizer2611, 0, wx.EXPAND, 5 )


		self.m_wizPage4.SetSizer( bSizer2621 )
		self.m_wizPage4.Layout()
		bSizer2621.Fit( self.m_wizPage4 )
		self.Centre( wx.BOTH )


		# Connect Events
		self.m_osu_dir.Bind( wx.EVT_DIRPICKER_CHANGED, self.update_osu_folder )
	def add_page(self, page):
		if self.m_pages:
			previous_page = self.m_pages[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.m_pages.append(page)

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def update_osu_folder( self, event ):
		event.Skip()


