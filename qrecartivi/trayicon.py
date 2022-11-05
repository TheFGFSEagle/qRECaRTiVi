#!/usr/bin/python3
#-*-coding: utf-8-*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import SimpleQt as SQt

from qrecartivi import menus

class TrayIcon(SQt.TrayIcon):
	def __init__(self):
		SQt.TrayIcon.__init__(self, iconFile=":/images/icon.png")
	
		menu = menus.trayMenu()
		self.setContextMenu(menu)
		self.show()
		
		self.clicked.connect(QtWidgets.qApp.mainWindow.toggle)
