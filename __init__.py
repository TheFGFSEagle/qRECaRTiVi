#!/usr/bin/python3
#-*-coding: utf-8-*-

import sys

if sys.version_info[0:2] < (3, 2):
	print("Sorry, but this application requires to be run with Python 3.2 or newer. Exiting")
	sys.exit(1)

import signal
import logging
logging.basicConfig(format='\n\n%(levelname)s at %(asctime)s from %(pathname)s:%(lineno)d: %(message)s', level=logging.DEBUG)

from PyQt5 import QtWidgets

from qrecartivi.application import Application

def main():
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	QtWidgets.qApp = Application()
	
	# DO NOT MOVE TO THE TOP - mainwindow must be imported AFTER overriding QtWidgets.qApp
	from qrecartivi.mainwindow import MainWindow
	QtWidgets.qApp.mainWindow = MainWindow()
	QtWidgets.qApp.mainWindow.initUI()
	QtWidgets.qApp.mainWindow.show()
	# DO NOT MOVE TO THE TOP - trayicon must be imported AFTER creating main window
	from qrecartivi.trayicon import TrayIcon
	QtWidgets.qApp.trayIcon = TrayIcon()
	
	sys.exit(QtWidgets.qApp.exec_())
