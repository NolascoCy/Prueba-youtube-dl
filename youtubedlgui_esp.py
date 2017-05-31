#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: Luis J. Aguilar
import sys
reload(sys)  # Reload does the trick for reencode !  
sys.setdefaultencoding('UTF8')  #por ejemplo si un nombre en spanish va tildado

#Consideraciones Previas en Debian Tener instalado lo siguiente: 
# python 2.7,  youtube-dl	
#To install youtube-dl	 it right away for all UNIX users (Linux, OS X, etc.) type as root: 
#  curl https://yt-dl.org/downloads/2015.03.03.1/youtube-dl -o /usr/local/bin/youtube-dl
# chmod a+x /usr/local/bin/youtube-dl

# agregar repositorio multimedia en /etc/apt/sources.list
# deb http://www.deb-multimedia.org jessie main non-free

#  aptitude update && aptitude install deb-multimedia-keyring
#
# aptitude install ffmpeg
from subprocess import *


###########################################################################
## Python code generated with wxFormBuilder (version Apr 20 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from threading import Thread
import time
#from time import sleep 
from random import choice 

# Define una variable tipo wx para la notificacion  del evento  en la ejecucion del thread 
EVT_RESULT_ID = wx.NewId()

def EVT_RESULT(win, func):
    """Define Resultado del Evento"""
    win.Connect(-1, -1, EVT_RESULT_ID, func)

class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data
########################################################################
class ThreadDescarga(Thread):
    """Clae Thread para el hilo de descarga."""
        
    #----------------------------------------------------------------------
    def __init__(self, wxObject,videostring):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.wxObject = wxObject
        
        self.videostring=videostring
        print  self.videostring
        self.start()    # inicia el hilo

    #----------------------------------------------------------------------
    def run(self):
		"""Run Worker Thread."""
        # This is the code executing in the new thread.
		texto=''
		texto2=''
		textout=''
		result = Popen(self.videostring, shell=True, stdout=PIPE)
		for i in result.stdout:
			textout=i.decode(sys.getdefaultencoding()).rstrip()
			texto=texto+str(i)+"\n"

			texto2=str(textout)+"\n"
		print texto2
		self.info=" Descargado "+texto2
		wx.PostEvent(self.wxObject, ResultEvent(self.info))
		
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		title='Descargar desde Youtube'
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2.AddSpacer( ( 50, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Descargar con youtube-dl", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		
		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		fgSizer2.AddSpacer( ( 50, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"URL Video", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.txt_Url = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,30 ), 0 )
		fgSizer2.Add( self.txt_Url, 0, wx.ALL, 5 )
		
		self.btn_Descargar = wx.Button( self, wx.ID_ANY, u"Descargar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_Descargar, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Seleccione:", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		fgSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		m_radioBox1Choices = [ u"Video", u"Solo Audio (MP3)" ]
		self.radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"Tipo", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.radioBox1.SetSelection( 0 )
		fgSizer2.Add( self.radioBox1, 0, wx.ALL, 5 )
		
		fgSizer2.AddSpacer( ( 1, 0), 1, wx.EXPAND, 5 )

		fgSizer2.AddSpacer( ( 1, 0), 1, wx.EXPAND, 5 )
		self.displayLbl = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.displayLbl, 0, wx.ALL, 5 )
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_Descargar.Bind( wx.EVT_BUTTON, self.Descargar )
		self.radioBox1.Bind( wx.EVT_RADIOBOX, self.sel_Opcion )
		
		# Manejador de eventos para los resultados del thread
		EVT_RESULT(self, self.updateDisplay)
		
	def __del__( self ):
		pass
	def sel_Opcion( self, event ):
		rb = event.GetEventObject() 
		print self.radioBox1.GetStringSelection()


		
	# Virtual event handlers, overide them in your derived class
	def Descargar( self, event ):
		download=self.txt_Url.GetValue()
		
		if(self.radioBox1.GetStringSelection()=='Video'):
			videostring="youtube-dl "+download
		else:
			videostring="youtube-dl -x --audio-format mp3 "+download
		ThreadDescarga(self,videostring)
		
	 #----------------------------------------------------------------------
	def updateDisplay(self, msg):
		"""Recibe datos del Thread y actualiza el mensaje en pantalla"""
		t = msg.data		
		self.displayLbl.SetLabel("%s" % t)
		self.txt_Url.SetValue("")
          
	
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame1(None)
        self.SetTopWindow(frame)
        frame.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
