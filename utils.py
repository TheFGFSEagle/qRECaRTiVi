#!/usr/bin/python3
#-*-coding: utf-8-*-

import os
import functools
import logging

from PyQt5.QtCore import QStandardPaths

logger = logging.getLogger()

def logFuncNameAndArgs(func):
	@functools.wraps(func)
	def call(*args, **kwargs):
		message = f"\n\nCalling {func.__name__}"
		if len(args) + len(kwargs.keys()) == 0:
			message += " without arguments"
		if len(args) > 0:
			message += f"""\n
Positional arguments:
{' '.join(map(repr, args))}"""
		if len(kwargs.keys()) > 0:
			message += f"""\n
Keyword arguments:
{' '.join([f'{key} : {repr(value.strip())}' for key, value in kwargs.items()])}"""
		logging.debug(message)
		func(*args, **kwargs)
	return call

# create a function synonyme
qreclog = logFuncNameAndArgs


def getDatadir():
	"""Returns a path to the directory where data files should be saved
	"""
	custom_datadir = os.environ.get("QRECARTIVI_DATADIR", "")
	if custom_datadir:
		return custom_datadir
	
	datadir = os.path.join(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation), "qrecartivi")
	
	if not os.path.isdir(datadir):
		os.makedirs(datadir, exist_ok=True)
	
	return datadir

def isPath(s):
	"""Finds out whether a string is an URL or a path
	@param s string containing a path or url
	@return True if it's a path, False if it's an url'
	"""
	if os.path.exists(s): # if a file with name s exists, we don't check any further and just return True
		return True
	elif s.startswith("/"): # clearly a path, urls never start with a slash
		return True
	elif "://" in s.split(".")[0]: # if a protocol is present, it's an url
		return False
	elif "localhost" in s: # special case for localhost domain name where splits on . would fail
		return False
	elif len(s.split("/")[0].split(".")) > 1: # dots before the first slash, normally separating TLD and domain name
		return False
	elif len(s.split("/")[0].split(":")) > 1: # if colons are present, either it's a IPv6 adress or there is a port number
		return False
	else: # all possible cases of an url checked, so it must be a path
		return True
