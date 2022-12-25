#!/usr/bin/env python
#-*- coding:utf-8 -*-

from .pyconsole import PythonConsoleDialog
from .settings import SettingsDialog

_dialogRegistry = {}

def get(cls):
	h = hash(cls)
	if not h in _dialogRegistry:
		_dialogRegistry[h] = cls()
	return _dialogRegistry[h]

