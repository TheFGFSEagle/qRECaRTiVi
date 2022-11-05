#!/usr/bin/env python
#-*- coding:utf-8 -*-

import logging

from PyQt5.QtWidgets import *

class StatusMessage:
	def __init__(self):
		pass
	
	def show(self, message, level, timeout=0):
		color = self.mapColor(level)
		qApp.mainWindow.sBar.showMessage(f"<span color='{color}'>{message}</span>", timeout)
		
	def mapColor(self, level):
		return {
			logging.DEBUG:	"blue",
			logging.INFO:	"black",
			logging.WARN:	"orange",
			logging.ERROR:	"red",
			logging.FATAL:	"violet",
		}[level]

class StatusMessageIcon(QLabel):
	def __init__(self, *args, **kwargs):
		QLabel.__init__(self, *args, **kwargs)
	
	def setIcon(self, level):
		mapping = {
			logging.DEBUG:	"debug",
			logging.INFO:	"information",
			logging.WARN:	"warning",
			logging.ERROR:	"error",
			logging.FATAL:	"fatal-error",
		}
		
		self.setStandardIcon(mapping[level])

class StatusBar(QStatusBar):
	def __init__(self, *args, **kwargs):
		QStatusBar.__init__(self, *args, **kwargs)
		
		self.message = StatusMessage()
		
		self.icon = StatusMessageIcon(parent=self)
		self.addPermanentWidget(self.icon)
	
	def showMessage(self, message, level, timeout=0):
		self.icon.setIcon(level)
		self.message.show(message, level, timeout)

