#!/usr/bin/python3
#-*-coding: utf-8-*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import SimpleQt as SQt

from qrecartivi import menus
from qrecartivi.tabs import *


class MainWindow(SQt.MainWindow):
	def __init__(self):
		SQt.MainWindow.__init__(self, title="qRECaRTiVi", iconFile=":/images/icon.png")
		
		self.mBar = self.menuBar()
		self.fileMenu = menus.fileMenu()
		self.mBar.addMenu(self.fileMenu)
		
		self.sBar = self.statusBar()
	
	def initUI(self):
		self.tabs = QTabWidget(self)
		self.widget().addWidget(self.tabs)
		self.abosTab = abos.AbosTab()
		self.tabs.addTab(self.abosTab, "Abos")
