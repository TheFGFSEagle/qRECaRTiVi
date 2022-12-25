#!/usr/bin/python3
#-*-coding: utf-8-*-

from PyQt5.QtWidgets import QMenu

import SimpleQt as SQt

import qrecartivi
import qrecartivi.dialogs


def trayMenu():
	menu = QMenu()
	menu.setTitle("Tray menu")
	menu.quit = SQt.ImageMenuItem(parent=menu, text="Quit", themeIconId="application-exit",
		action=qrecartivi.app.quit
	)
	return menu

def fileMenu():
	menu = QMenu()
	menu.setTitle("File")
	menu.reload = SQt.ImageMenuItem(
		parent=menu, text="Reload abos", themeIconId="reload",
		action=lambda args: qrecartivi.mainWindow.abosTab.updateAboList()
	)
	menu.prefs = SQt.ImageMenuItem(
		parent=menu, text="Preferences", themeIconId="preferences",
		action=lambda args: qrecartivi.dialogs.get(qrecartivi.dialogs.SettingsDialog).show()
	)
	menu.quit = SQt.ImageMenuItem(parent=menu, text="Quit", themeIconId="application-exit",
		action=qrecartivi.app.quit
	)
	return menu

def debugMenu():
	menu = QMenu()
	menu.setTitle("Debugging")
	menu.pyconsole = SQt.ImageMenuItem(
		parent=menu, text="Open integrated Python console", themeIconId="application-exec",
		action=lambda args: qrecartivi.dialogs.get(qrecartivi.dialogs.PythonConsoleDialog).show()
	)
	return menu

