#!/usr/bin/python3
#-*-coding: utf-8-*-

import os
import functools
import logging
import inspect
import appdirs

logger = logging.getLogger()

def logFunctionOrMethodNameAndArgs(func):
	@functools.wraps(func)
	def call(*args, **kwargs):
		message = f"\n\nCalling {func.__qualname__.replace('__main__.', '')}"
		if len(args) + len(kwargs.keys()) == 0:
			message += " without arguments"
		if len(args) > 0:
			message += f"""\n
Positional arguments:
{' '.join(map(repr, args))}"""
		if len(kwargs.keys()) > 0:
			message += f"""\n
Keyword arguments:
{' '.join([f'{key} : {repr(value).strip()}' for key, value in kwargs.items()])}"""
		logging.debug(message)
		return func(*args, **kwargs)
	return call

# shorthand
qreclog = logFunctionOrMethodNameAndArgs

@qreclog
def getDataDir():
	"""Returns a path to the directory where data files should be saved
	"""
	datadir = os.environ.get("QRECARTIVI_DATADIR", "")
	if not datadir:
		datadir = appdirs.user_data_dir("qrecartivi")
	
	os.makedirs(datadir, exist_ok=True)
	
	return datadir

@qreclog
def getConfigDir():
	"""Returns a path to the directory where data files should be saved
	"""
	configdir = os.environ.get("QRECARTIVI_CONFIGDIR", "")
	if not configdir:
		configdir = appdirs.user_config_dir("qrecartivi")
	
	os.makedirs(configdir, exist_ok=True)
	
	return configdir

@qreclog
def isPath(s):
	"""Finds out whether a string is an URL or a path
	@param s string containing a path or url
	@return True if it's a path, False if it's an url'
	"""
	if os.path.exists(s): # if a file with name s exists, we don't check any further and just return True
		return True
	elif s.startswith("/"): # clearly a path, urls never start with a slash
		return True
	elif s.startswith("file://"):
		return True
	elif "://" in s.split(".")[0]: # if a protocol is present, it's an url
		return False
	elif "localhost" in s[:30]: # special case for localhost domain name where splits on . would fail
		return False
	elif len(s.split("/")[0].split(".")) > 1: # dots before the first slash, normally separating TLD and domain name
		return False
	elif len(s.split("/")[0].split(":")) > 1: # if colons are present, either it's a IPv6 adress or there is a port number
		return False
	else: # all possible cases of an url checked, so it must be a path
		return True
