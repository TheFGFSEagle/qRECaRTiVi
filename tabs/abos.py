#!/usr/bin/python3
#-*-coding: utf-8-*-

import logging
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import SimpleQt as SQt
from qrecartivi import utils

from qrecartivi.utils import qreclog

logger = logging.getLogger()

class ChannelData(object):
	"""Data class for a channel
	"""
	def __init__(self, name, owner, description, episodes, image=None):
		object.__init__(self)
		
		self.name = name
		self.owner = owner
		self.description = description
		self.image = image
		self.episodes = episodes

class ChannelEpisodeData(object):
	"""Data class for a channel's episode
	"""
	def __init__(self, title, date, time, duration, author, owner, description, image=None):
		object.__init__(self)
		
		self.title = title
		self.date = date
		self.time = time
		self.duration = duration
		self.author = author
		self.owner = owner
		self.description = description

class ChannelWidget(SQt.HBox):
	"""Widget to display important channel data such as owner, name, etc.
	"""
	def __init__(self, data, parent, **kwargs):
		SQt.HBox.__init__(self, parent=parent, **kwargs)
		
		self.parent = parent
		self.data = data
		
		#iconLabel = QLabel(pixmap=self.data.icon)
		#self.addWidget(iconLabel)
		self.nameLabel = QLabel(self.data.name)
		self.addWidget(self.nameLabel)
		
		self.ownerLabel = QLabel(self.data.owner)
		self.addWidget(self.ownerLabel)
		
		self.descriptionLabel = QLabel(self.data.description)
		self.addWidget(self.descriptionLabel)
		
		self.episodeCountLabel = QLabel(str(len(self.data.episodes)))
		self.addWidget(self.episodeCountLabel)
		
	@qreclog
	def mouseReleaseEvent(self, *args):
		"""Update displayed channel episode data on mouse click
		"""
		self.parent.displayChannelDetails(self.data)

class ChannelEpisodeWidget(SQt.HBox):
	def __init__(self, data, **kwargs):
		SQt.HBox.__init__(self, **kwargs)
		
		self.data = data
		
		self.titleLabel = QLabel(self.data.title)
		self.addWidget(self.titleLabel)

class AbosTab(QSplitter):
	def __init__(self, parent=None):
		QSplitter.__init__(self, parent)
		
		self.channels = [ChannelData("Example", "PyQt5", "Description", [ChannelEpisodeData("First Episode", "18.05.21", "03:22", "1:00", "Fred", "PyQt5", "Description")])]
		self.channelListView = SQt.VBox(parent=self, scrollingEnabled=True)
		self.addWidget(self.channelListView)
		
		self.channelDetailsSplitter = QSplitter(self, orientation=Qt.Vertical)
		self.addWidget(self.channelDetailsSplitter)
		
		self.episodeListView = SQt.VBox(parent=self.channelDetailsSplitter, scrollingEnabled=True)
		self.channelDetailsSplitter.addWidget(self.episodeListView)
		
		self.channelDetailsView = SQt.VBox(parent=self.channelDetailsSplitter, scrollingEnabled=True)
		self.channelDetailsSplitter.addWidget(self.channelDetailsView)

	def updateAboList(self):
		self.channelListView.clearChildren()
		for channel in self.channels:
			channelWidget = ChannelWidget(channel, self)
			self.channelListView.addWidget(channelWidget)
	
	def displayChannelDetails(self, channel):
		"""Display the episodes of a channel in self.channelListView
		@param channel ChannelData instance
		"""
		self.episodeListView.clearChildren()
		for episode in channel.episodes:
			episodeWidget = ChannelEpisodeWidget(episode, parent=self)
			self.episodeListView.addWidget(episodeWidget)
		# TODO: add code to display channel information in self.channelDetailsView
