#!/usr/bin/python3
#-*-coding: utf-8-*-

from PyQt5.QtWidgets import *

import SimpleQt as SQt


def trayMenu():
	menu = QMenu()
	menu.setTitle("Tray menu")
	menu.quit = SQt.ImageMenuItem(parent=menu, text="Quit", themeIconId="application-exit", action=qApp.quit)
	return menu

def fileMenu():
	menu = QMenu()
	menu.setTitle("File")
	menu.reload = SQt.ImageMenuItem(parent=menu, text="Reload abos", themeIconId="reload", action=lambda _: qApp.mainWindow.abosTab.updateAboList())
	menu.prefs = SQt.ImageMenuItem(parent=menu, text="Preferences", themeIconId="preferences", action=print)
	menu.quit = SQt.ImageMenuItem(parent=menu, text="Quit", themeIconId="application-exit", action=qApp.quit)
	return menu
