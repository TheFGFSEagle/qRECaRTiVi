#!/usr/bin/python3
#-*-coding: utf-8-*-

import sys
import os
import logging

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
		sFile.close()
		
		self.setOrganizationName("Geisbergium")
		self.setApplicationName("qRECaRTiVi")
		self.setApplicationVersion("1.0")
		self.loc = os.path.dirname(os.path.abspath(__file__)) + "/"
		
		self.getCommandLineArgs()
		
		self.settings = QSettings()
		self.fontSize = self.settings.value("LookAndFeel/FontSize", 13)
		self.fontFamily = self.settings.value("LookAndFeel/FontFamily", "Ubuntu")
		self.setFont(QFont(self.fontFamily, self.fontSize))
	
	def showStatusMessage(self, message, level):
		getattr(
			logging,
			{
				logging.DEBUG:		"debug",
				logging.INFO:		"info",
				logging.WARN:		"warn",
				logging.ERROR:		"error",
				logging.FATAL:		"fatal",
			}[level]
		)(message)
		
		if hasattr(qApp, "mainwindow"):
			qApp.mainWindow.sBar.showMessage(message, level)
	
	def quit(self, *args, **kwargs):
		QApplication.quit()
	
	def getCommandLineArgs(self):
		self.argp = QCommandLineParser()
		self.argp.addHelpOption()
		self.argp.addVersionOption()
		self.argp.setApplicationDescription("qRECaRTiVi - records any audio / video stream and downloads podcasts from RSS files")
		
		logLevelOption = QCommandLineOption("loglevel", "Set logging level (one of DEBUG, INFO, WARNING, ERROR, FATAL)", "LOGLEVEL", "INFO")
		self.argp.addOption(logLevelOption)
		
		self.argp.process(self)
		
		self.cmdArgs = {}
		self.cmdArgs["loglevel"] = self.argp.value("loglevel").upper()
		
		if self.cmdArgs["loglevel"] not in ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"]:
			print(f"Loglevel {self.argp.value(logLevelOption)} is not one of DEBUG, INFO, WARN, ERROR, FATAL - using default of WARNING")
			self.cmdArgs["loglevel"] = "WARN"
		
