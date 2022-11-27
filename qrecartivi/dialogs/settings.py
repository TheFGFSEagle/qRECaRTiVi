#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import QDialogButtonBox, QLabel

import SimpleQt

class SettingsDialog(SimpleQt.SettingsDialog):
	def __init__(self):
		SimpleQt.SettingsDialog.__init__(self)
		
		self.addSetting("Test A", "/test/a", bool)
		self.addSetting("Test B", "/test/b", int)
		self.addSetting("Test C", "/test/d", float)
		self.addSetting("Test D", "/test/c", str)
		self.addSetting("Test E", "/test/d", range, min=0, max=50, step=3)
		self.addSetting("Test F", "/test/f", range, min=0.0, max=10.5, step=0.8395)
		self.addSetting("Test G", "/test/g", list, items=["A", "B", "C", "D"])
		
