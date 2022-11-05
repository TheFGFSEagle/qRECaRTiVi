#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt5.QtWidgets import qApp

from qrecartivi.addons import addon

class AddonManager:
	def __init__(self):
		self.__addons = []
	
	def addAddon(self, ident):
		oldPath = list(sys.path)
		sys.path.append(os.path.join(utils.getDatadir(), "addons"))
		module = __import__(ident)
		self.__addons[ident] = module.Addon()
		self.__addons[ident].initialize()
		sys.path = oldPath
	
	def removeAddon(self, ident):
		if ident in self.__addons:
			self.__addons[ident].remove()

