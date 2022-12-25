#!/usr/bin/python3
#-*-coding: utf-8-*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import SimpleQt as SQt

import qrecartivi
from qrecartivi import menus
from qrecartivi.tabs import *
from qrecartivi.statusbar import StatusBar


class MainWindow(SQt.MainWindow):
	def __init__(self):
		SQt.MainWindow.__init__(self, title="qRECaRTiVi", iconFile=":/images/icon.png")
		
		self.mBar = self.menuBar()
		self.fileMenu = menus.fileMenu()
		self.mBar.addMenu(self.fileMenu)
		self.debugMenu = menus.debugMenu()
		self.mBar.addMenu(self.debugMenu)
		
		self.sBar = StatusBar()
	
	def initUI(self):
		self.tabs = QTabWidget(self)
		self.widget().addWidget(self.tabs)
		self.abosTab = abos.AbosTab()
		self.tabs.addTab(self.abosTab, "Abos")
	
	def closeEvent(self, event):
		qrecartivi.app.quit()
