# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar 14 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GRIB Downloader", pos = wx.DefaultPosition, size = wx.Size( 500,230 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Weather Model", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		m_choiceWeatherModelChoices = [ u"Météo France", u"OpenSkiron" ]
		self.m_choiceWeatherModel = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceWeatherModelChoices, 0 )
		self.m_choiceWeatherModel.SetSelection( 0 )
		fgSizer1.Add( self.m_choiceWeatherModel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Model Precision", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		m_choiceModelPrecisionChoices = [ u"Arome (0,025° / 2 days)", u"Arpege (0,1° / 4 days)" ]
		self.m_choiceModelPrecision = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceModelPrecisionChoices, 0 )
		self.m_choiceModelPrecision.SetSelection( 0 )
		fgSizer1.Add( self.m_choiceModelPrecision, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Zone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		m_choiceZoneChoices = [ u"Hyères", u"Golf du Lion - Sardaigne" ]
		self.m_choiceZone = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceZoneChoices, 0 )
		self.m_choiceZone.SetSelection( 0 )
		fgSizer1.Add( self.m_choiceZone, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"GRIB Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_folder = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_folder, 1, wx.ALL, 5 )
		
		self.m_buttonFolder = wx.Button( self, wx.ID_ANY, u"Choose Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_buttonFolder, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( fgSizer1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonDownload = wx.Button( self, wx.ID_ANY, u"Download GRIB", wx.DefaultPosition, wx.Size( 170,50 ), 0 )
		self.m_buttonDownload.SetDefault() 
		bSizer1.Add( self.m_buttonDownload, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_choiceWeatherModel.Bind( wx.EVT_CHOICE, self.onWeatherModelChoice )
		self.m_choiceModelPrecision.Bind( wx.EVT_CHOICE, self.onPrecisionChoice )
		self.m_choiceZone.Bind( wx.EVT_CHOICE, self.onZoneChoice )
		self.m_buttonFolder.Bind( wx.EVT_BUTTON, self.onFolderClick )
		self.m_buttonDownload.Bind( wx.EVT_BUTTON, self.onDownloadClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onWeatherModelChoice( self, event ):
		event.Skip()
	
	def onPrecisionChoice( self, event ):
		event.Skip()
	
	def onZoneChoice( self, event ):
		event.Skip()
	
	def onFolderClick( self, event ):
		event.Skip()
	
	def onDownloadClick( self, event ):
		event.Skip()
	

