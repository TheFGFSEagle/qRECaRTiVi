#!/usr/bin/python3
#-*-coding: utf-8-*-

import sys, os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from qrecartivi import resources

if not any([s in sys.argv for s in ("--style", "-style")]):
	sys.argv += ["--style", "Fusion"]

class Application(QApplication):
	def __init__(self):
		QApplication.__init__(self, sys.argv)
		
		sFile = QFile(":/style.qss")
		sFile.open(QIODevice.ReadOnly)
		self.setStyleSheet(QTextStream(sFile).readAll())
		
		self.setOrganizationName("Geisbergium")
		self.setApplicationName("qRECaRTiVi")
		self.setApplicationVersion("1.0")
		self.loc = os.path.dirname(os.path.abspath(__file__)) + "/"
		
		sFile = QFile(":/style.qss")
		sFile.open(QIODevice.ReadOnly)
		self.setStyleSheet(QTextStream(sFile).readAll())
		sFile.close()
		
		self.setupArgParser()
		self.procArgs()
		
		self.settings = QSettings()
		self.fontSize = self.settings.value("LookAndFeel/FontSize", 13)
		self.fontFamily = self.settings.value("LookAndFeel/FontFamily", "Ubuntu")
		self.setFont(QFont(self.fontFamily, self.fontSize))
	
	def procArgs(self):
		pass
	
	def quit(self, *args, **kwargs):
		QApplication.quit()
	
	def setupArgParser(self):
		self.argp = QCommandLineParser()
		self.argp.addHelpOption()
		self.argp.addVersionOption()
		self.argp.setApplicationDescription("qRECaRTiVi - records any audio / video stream and downloads podcasts from RSS files")
		self.argp.process(self)
