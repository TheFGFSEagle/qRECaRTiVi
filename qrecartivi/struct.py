#!/usr/bin/env python
#-*- coding:utf-8 -*-

from qrecartivi import utils

class ChannelData:
	"""Data class for a channel
	"""
	@utils.qreclog
	def __init__(self, name, owner, description, episodes, image=None):
		self.name = name
		self.owner = owner
		self.description = description
		# TODO: add thumbnail displaying support
		self.image = image
		self.episodes = episodes
		self.attrs = list(vars(self))


class ChannelEpisodeData:
	"""Data class for a channel's episode
	"""
	@utils.qreclog
	def __init__(self, title, date, time, duration, author, owner, description, image=None):
		self.title = title
		self.date = date
		self.time = time
		self.duration = duration
		self.author = author
		self.owner = owner
		self.description = description
		self.attrs = list(vars(self))

