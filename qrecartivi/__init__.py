#!/usr/bin/python3
#-*-coding: utf-8-*-

import sys
import logging

logging.basicConfig(
	format='\n\n%(levelname)s at %(asctime)s from %(pathname)s:%(lineno)d:\n\t%(message)s',
	level=logging.WARNING
)

if sys.version_info[0:2] < (3, 6):
	logging.fatal("Sorry, but this application requires to be run with Python 3.6 or newer. Exiting")
	sys.exit(1)

import signal


from PyQt5 import QtWidgets

from qrecartivi.application import Application
from qrecartivi.mainwindow import MainWindow
from qrecartivi.trayicon import TrayIcon
from qrecartivi.dialogs.settings import SettingsDialog
from qrecartivi.addons.addonmanager import AddonManager

app = None
mainWindow = None
trayIcon = None
settingsDialog = None
addonManager = None

def main():
	global app, mainWindow, trayIcon, settingsDialog, addonManager
	
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	app = Application()
	app.init()
	
	mainWindow = MainWindow()
	mainWindow.initUI()
	mainWindow.show()
	
	trayIcon = TrayIcon()
	trayIcon.initUI()
	
	settingsDialog = SettingsDialog()
	
	addonManager = AddonManager()
	
	sys.exit(app.exec_())
