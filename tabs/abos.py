#!/usr/bin/python3
#-*-coding: utf-8-*-

import logging
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import SimpleQt as SQt

from qrecartivi import utils

logger = logging.getLogger()


class ChannelData(object):
	"""Data class for a channel
	"""
	@utils.qreclog
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
	@utils.qreclog
	def __init__(self, title, date, time, duration, author, owner, description, image=None):
		object.__init__(self)
		
		self.title = title
		self.date = date
		self.time = time
		self.duration = duration
		self.author = author
		self.owner = owner
		self.description = description


class ChannelWidget(QListWidgetItem):
	"""Widget to display important channel data such as owner, name, etc.
	"""
	@utils.qreclog
	def __init__(self, data, parent, **kwargs):
		QListWidgetItem.__init__(self, parent=parent, **kwargs)
		
		self.parent = parent
		self.data = data
		
		# iconLabel = QLabel(pixmap=self.data.icon)
		# self.addWidget(iconLabel)
		self.nameLabel = QLabel(self.data.name)
		self.addWidget(self.nameLabel)
		
		self.ownerLabel = QLabel(self.data.owner)
		self.addWidget(self.ownerLabel)
		
		self.descriptionLabel = QLabel(self.data.description)
		self.addWidget(self.descriptionLabel)
		
		self.episodeCountLabel = QLabel(str(len(self.data.episodes)))
		self.addWidget(self.episodeCountLabel)


class ChannelEpisodeWidget(SQt.HBox):
	@utils.qreclog
	def __init__(self, data, **kwargs):
		SQt.HBox.__init__(self, **kwargs)
		
		self.data = data
		
		self.titleLabel = QLabel(self.data.title)
		self.addWidget(self.titleLabel)


class AbosTab(QSplitter):
	@utils.qreclog
	def __init__(self, parent=None):
		QSplitter.__init__(self, parent)
		
		self.channels = [ChannelData("Example", "PyQt5", "Description", [ChannelEpisodeData("First Episode", "18.05.21", "03:22", "1:00", "Fred", "PyQt5", "Description")])]
		self.channelsView = QListWidget(parent=self)
		self.addWidget(self.channelsView)
		
		self.channelDetailsSplitter = QSplitter(self, orientation=Qt.Vertical)
		self.addWidget(self.channelDetailsSplitter)
		
		self.episodesView = QListWidget(parent=self.channelDetailsSplitter)
		self.channelDetailsSplitter.addWidget(self.episodesView)
		
		self.channelDetailsView = SQt.VBox(parent=self.channelDetailsSplitter)
		self.channelDetailsSplitter.addWidget(self.channelDetailsView)
	
	@utils.qreclog
	def updateAboList(self):
		"""
		Reload the list of channels
		"""
		self.channelsView.clear()
		for channel in self.channels:
			channelWidget = ChannelWidget(channel, self.channelsView)
			self.channelsView.addWidget(channelWidget)
	
	@utils.qreclog
	def displayChannelDetails(self, channel):
		"""Display the episodes of a channel in self.channelListView
		@param channel ChannelData instance
		"""
		self.episodesView.clearChildren()
		for episode in channel.episodes:
			episodeWidget = ChannelEpisodeWidget(episode, parent=self.episodesView)
			self.episodesView.addWidget(episodeWidget)
		# TODO: add code to display channel information in self.channelDetailsView
