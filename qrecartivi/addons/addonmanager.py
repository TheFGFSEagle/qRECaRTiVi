#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from importlib import import_module

from SimpleQt import settings

from qrecartivi import utils
from qrecartivi.addons import addon

class AddonManager:
	def __init__(self):
		self.__addons = []
		self.custom_addon_paths = settings.get("addons/path", [])
	
	def getAddonPaths(self):
		paths = self.custom_addon_paths + [os.path.join(utils.getDataDir(), "addons")]
		paths += list(filter(None, os.environ.get("QRECARTIVI_ADDONPATH", "").split(os.pathsep)))
		return list(map(os.path.abspath, paths))
	
	def addAddonPath(self, path):
		if path not in self.custom_addon_paths:
			self.custom_addon_paths.append(path)
		self._write_custom_addon_paths_to_settings()
	
	def removeAddonPath(self, path):
		if path in self.custom_addon_paths:
			self.custom_addon_paths.remove(path)
		self._write_custom_addon_paths_to_settings()
	
	def _write_custom_addon_paths_to_settings(self):
		qrecartivi.app.setting.set("addons/path", self.custom_addon_paths)
		
	def addAddon(self, ident):
		if ident in self.__addons:
			raise addon.AddonRegisteredException(ident)
		
		oldPath = list(sys.path)
		sys.path += self.getAddonPaths()
		module = import_module(ident)
		self.__addons[ident] = module.Addon()
		self.__addons[ident].initialize()
		sys.path = oldPath
		
		qrecartivi.app.settings.set("addons/{ident}/enabled", True)
	
	def toggleAddon(self, ident, state=None):
		if ident not in self.__addons:
			raise addon.AddonUnknownException(ident)
		
		state = self.__addons[ident].toggleEnabled(state=state)
		qrecartivi.app.settings.set("addons/{ident}/enabled", state)
		return state
		
	def removeAddon(self, ident):
		if ident not in self.__addons:
			raise addon.AddonUnknownException(ident)
		
		self.__addons[ident].remove()
		qrecartivi.app.settings.remove(f"addons/{ident}")

