#!/usr/bin/env python
#-*- coding:utf-8 -*-

class AddonException(Exception):
	def __init__(self, ident):
		self.ident = ident

class AddonRegisteredException(AddonException):
	def __str__(self):
		return f"AddonRegisteredException: addon with ID {self.ident} is already registered"

class AddonUnknownException(AddonException):
	def __str__(self):
		return f"AddonUnknownException: no addon with ID {self.ident} is registered"


class Addon:
	def __init__(self, cfg):
		self.cfg = cfg
	
	def getChannels(self):
		return []
	
