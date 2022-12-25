#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

import SimpleQt
from SimpleQt.dialogs.settings import SettingsDialog, ListSetting, Setting
from SimpleQt import settings, VBox

import qrecartivi
from qrecartivi.addons.addonmanager import AddonManager

class SettingsDialogAddonsList(ListSetting):
	def __init__(self, text="Addons", path="/addons", selectionMode=QListWidget.SingleSelection,
					itemFlags=Qt.ItemIsUserCheckable, default=None):
		Setting.__init__(self, text, path, default)
		
		self.widget = QListWidget()
		self.widget.setSelectionMode(selectionMode)
		self.addWidget(self.widget)
		
		self.buttonsBox = VBox()
		self.addWidget(self.buttonsBox)
		
		self.widget.currentRowChanged.connect(lambda text: self.changed.emit(self))
		self.widget.itemClicked.connect(lambda item: print("itemChanged", dir(item)))
		settings.getNode("/addons").addListener(lambda n, subn: self.update(), True)
		self.update()
	
	def update(self):
		self.widget.clear()
		for addon in AddonManager().getAddons().values():
			item = QListWidgetItem(addon.cfg.getStringValue("name", f"Unnamed addon {self.widget.count() + 1}"), self.widget)
			item.setCheckState(Qt.Checked if addon.cfg.getBoolValue("enabled", False) else Qt.Unchecked)

class SettingsDialog(SettingsDialog):
	def __init__(self):
		SimpleQt.SettingsDialog.__init__(self)
		
		self.addPage("general", "General")
		
		fontSetting = self.addSetting(
			"general", "Font", "/gui/font", QFont, 
			QFont(settings.getStringValue("/gui/font/family", "Ubuntu"), settings.getIntValue("/gui/font/size", 13))
		)
		fontSetting.widget.fontChanged.connect(lambda font: qrecartivi.app.setFont(font))
		fontSetting.reset.connect(lambda setting: qrecartivi.app.setFont(setting.value()))
		
		page = self.addPage("addons", "Addons")
		page.addWidget(SettingsDialogAddonsList())

