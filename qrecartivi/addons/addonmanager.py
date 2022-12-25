#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import importlib.util
from hashlib import md5

from simple_singleton import Singleton

from SimpleQt import settings

from pyproptree import io

from qrecartivi import utils
from qrecartivi.addons import addon

class AddonManager(metaclass=Singleton):
	_instance = None
	def __init__(self):
		self._addons = {}
		settings.initNode("/addons/path", str, os.path.abspath(os.path.join(utils.getDataDir(), "addons")))
		for i, path in enumerate(filter(None, os.environ.get("QRECARTIVI_ADDONPATH", "").split(os.pathsep))):
			settings.initNode(f"/addons/path", str, os.path.abspath(path))
		settings.addListener("/addons", self.updateAddons, True)
		self.reloadAddons()
	
	def reloadAddons(self):
		for ident in self._addons:
			self._addons[ident].shutdown()
		
		for c in settings.getNode("/addons").getChildren("path"):
			os.makedirs(c.getStringValue(), exist_ok=True)
			for f in os.listdir(c.getStringValue()):
				f = os.path.join(c.getStringValue(), f)
				if f.endswith("addon.xml") and not os.path.isdir(f):
					self.loadAddon(f)
	
	def updateAddons(self):
		for addon in self._addons:
			addon.update()
	
	def getAddonPaths(self):
		return list(map(lambda n: n.getStringValue(), settings.getNode("/addons").getChildren("path")))
	
	def addAddonPath(self, path):
		settings.initNode("/addons/path", str, path)
	
	def removeAddonPath(self, path):
		for n in settings.getNode("/addons").getChildren("path"):
			if path == n.getStringValue():
				n.remove()
	
	def getAddons(self):
		return self._addons
	
	def loadAddon(self, path):
		cfg = io.loadFile(path)
		ident = cfg.getStringValue("ident", "addon_" + md5(path.encode("ascii")).hexdigest())
		script = os.path.join(os.path.dirname(path), cfg.getStringValue("script", None))
		module = "qrecartivi.addons." + ident
		if ident == None:
			raise ValueError("cannot add addon with empty script path")
		if ident in self._addons:
			raise addon.AddonRegisteredException(ident)
		
		settings.addNode(f"/addons/{ident}", cfg)
		
		spec = importlib.util.spec_from_file_location(module, script)
		sys.modules[module] = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(sys.modules[module])
		self._addons[ident] = sys.modules[module].Addon(cfg)
		cfg.initNode("enabled", bool, True)
	
	def toggleAddon(self, ident, state=None):
		if ident not in self._addons:
			raise addon.AddonUnknownException(ident)
		
		state = self._addons[ident].cfg.getBoolValue("enabled", False)
		self._addons[ident].cfg.setValue("enabled", not state)
		return state
	
	def removeAddon(self, ident):
		if ident not in self._addons:
			raise addon.AddonUnknownException(ident)
		
		self._addons[ident].remove()

