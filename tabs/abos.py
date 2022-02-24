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
		# TODO: add thumbnail displaying support
		self.image = image
		self.episodes = episodes
		self.attrs = list(vars(self))


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
		self.attrs = list(vars(self))


class ChannelWidget(QWidget):
	"""Widget to display important channel data such as owner, name, etc.
	"""
	@utils.qreclog
	def __init__(self, data, **kwargs):
		QWidget.__init__(self, **kwargs)

		self.data = data
		
		# TODO: add thumbnail displaying support
		#self.thumbItem = QTableWidgetItem(pixmap=self.data.image)
		# self.addWidget(iconLabel)
		self.nameItem = QTableWidgetItem(self.data.name)
		
		self.ownerItem = QTableWidgetItem(self.data.owner)
		
		self.descriptionItem = QTableWidgetItem(self.data.description)
		
		self.episodeCountItem = QTableWidgetItem(str(len(self.data.episodes)))
		
		self.items = [self.nameItem, self.ownerItem, self.descriptionItem, self.episodeCountItem]
	
	@utils.qreclog
	def addItems(self, tableWidget, rowIndex):
		for i, item in enumerate(self.items):
			tableWidget.setItem(rowIndex, i, item)

class ChannelEpisodeWidget(QWidget):
	@utils.qreclog
	def __init__(self, data, **kwargs):
		QWidget.__init__(self, **kwargs)
		
		self.data = data
		
		self.titleItem = QTableWidgetItem(self.data.title)
		self.dateItem = QTableWidgetItem(self.data.date)
		self.timeItem = QTableWidgetItem(self.data.time)
		self.durationItem = QTableWidgetItem(self.data.duration)
		self.authorItem = QTableWidgetItem(self.data.author)
		self.ownerItem = QTableWidgetItem(self.data.owner)
		
		self.items = [self.titleItem, self.dateItem, self.timeItem, self.durationItem, self.authorItem, self.ownerItem]
		
	@utils.qreclog
	def addItems(self, tableWidget, rowIndex):
		for i, item in enumerate(self.items):
			tableWidget.setItem(rowIndex, i, item)


class ChannelsView(QTableWidget):
	@utils.qreclog
	def __init__(self, parent, **kwargs):
		QTableWidget.__init__(self, parent=parent, **kwargs)
		self.parent = parent
		self.itemSelectionChanged.connect(self.onItemSelectionChanged)
		self.setSelectionBehavior(QTableWidget.SelectRows)
		self.verticalHeader().hide()
		self.setColumnCount(4)
		
		# TODO: make columns remember width and order across restarts
		for i, size in zip(range(4), (140, 100, 200, 80)):
			self.setColumnWidth(i, size)
		
		self.setHorizontalHeaderLabels(["Name", "Owner", "Description", "Episodes"])
		self.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.setShowGrid(False)
	
	@utils.qreclog
	def onItemSelectionChanged(self):
		selectedItem = self.selectedItems()[0]
		self.parent.displayChannelDetails(selectedItem.row())


class EpisodesView(QTableWidget):
	@utils.qreclog
	def __init__(self, parent, **kwargs):
		QTableWidget.__init__(self, parent=parent, **kwargs)
		self.parent = parent
		self.itemSelectionChanged.connect(self.onItemSelectionChanged)
		self.setSelectionBehavior(QTableWidget.SelectRows)
		self.verticalHeader().hide()
		self.setColumnCount(6)
		
		# TODO: make columns remember width and order across restarts
		for i, size in zip(range(4), (120, 80, 80, 80, 120, 200)):
			self.setColumnWidth(i, size)
		
		self.setHorizontalHeaderLabels(["Name", "Date", "Time", "Duration", "Author", "Title"])
		self.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.setShowGrid(False)
	
	@utils.qreclog
	def onItemSelectionChanged(self):
		selectedItem = self.selectedItems()[0]
		self.parent.displayEpisodeDetails(selectedItem.row())


class ChannelDetailsView(SQt.VBox):
	@utils.qreclog
	def __init__(self, parent=None):
		SQt.VBox.__init__(self, parent=parent)
		
		self.parent = parent
		
		self.nameLabel = QLabel("Channel name")
		self.addWidget(self.nameLabel)
		self.ownerLabel = QLabel("Channel owner")
		self.addWidget(self.ownerLabel)
		self.descriptionLabel = QLabel("Channel description")
		self.addWidget(self.descriptionLabel)
	
	@utils.qreclog
	def displayChannelDetails(self, channel):
		self.nameLabel.setText(channel.name)
		self.ownerLabel.setText(channel.owner)
		self.descriptionLabel.setText(channel.description)

class EpisodeDetailsView(SQt.VBox):
	@utils.qreclog
	def __init__(self, parent=None):
		SQt.VBox.__init__(self, parent=parent)
		
		self.parent = parent
		
		self.titleLabel = QLabel("Episode title")
		self.addWidget(self.titleLabel)
		self.ownerLabel = QLabel("Episode owner")
		self.addWidget(self.ownerLabel)
		self.descriptionLabel = QLabel("Episode description")
		self.addWidget(self.descriptionLabel)
	
	@utils.qreclog
	def displayEpisodeDetails(self, episode):
		self.titleLabel.setText(episode.title)
		self.ownerLabel.setText(episode.owner)
		self.descriptionLabel.setText(episode.description)

class AbosTab(QSplitter):
	@utils.qreclog
	def __init__(self, **kwargs):
		QSplitter.__init__(self, **kwargs)
		
		self.channels = [ChannelData("Example", "PyQt5", "Description", [ChannelEpisodeData("First Episode", "18.05.21", "03:22", "1:00", "Fred", "PyQt5", "Description")] * 100), ChannelData("Example 2", "PyQt4", "Description 2", [ChannelEpisodeData("First Episode", "19.05.21", "04:22", "1:00", "Frederic", "PyQt4", "Description 2")] * 100)] * 100
		
		self.channelsSplitter = QSplitter(self, orientation=Qt.Vertical)
		self.addWidget(self.channelsSplitter)
		
		self.channelsView = ChannelsView(parent=self)
		self.channelsSplitter.addWidget(self.channelsView)
		
		self.channelDetailsView = ChannelDetailsView(parent=self.channelsSplitter)
		self.channelsSplitter.addWidget(self.channelDetailsView)
		
		self.episodesSplitter = QSplitter(self, orientation=Qt.Vertical)
		self.addWidget(self.episodesSplitter)
		
		self.episodesView = EpisodesView(parent=self)
		self.episodesSplitter.addWidget(self.episodesView)
		
		self.episodeDetailsView = EpisodeDetailsView(parent=self.episodesSplitter)
		self.episodesSplitter.addWidget(self.episodeDetailsView)
		
		self.updateAboList()
		self.displayChannelDetails(0)
	
	@utils.qreclog
	def updateAboList(self):
		"""
		Reload the list of channels
		"""
		self.channelsView.clear()
		# TODO: tell plugins to update self.channels once plugins are implemented
		self.channelsView.setRowCount(len(self.channels))
		
		for rowIndex, channel in enumerate(self.channels):
			channelWidget = ChannelWidget(channel, parent=self.channelsView)
			channelWidget.addItems(self.channelsView, rowIndex)
	
	@utils.qreclog
	def displayChannelDetails(self, channelIndex):
		"""Display the episodes of a channel in self.channels
		@param channelIndex index of ChannelData in self.channels
		"""
		self.currentChannelIndex = channelIndex
		self.episodesView.clear()
		self.episodesView.setRowCount(len(self.channels))
		for rowIndex, episode in enumerate(self.channels[channelIndex].episodes):
			episodeWidget = ChannelEpisodeWidget(episode, parent=self.episodesView)
			episodeWidget.addItems(self.episodesView, rowIndex)
		self.channelDetailsView.displayChannelDetails(self.channels[channelIndex])
		
	def displayEpisodeDetails(self, episodeIndex):
		"""Display the description etc. of an episode in self.channels[channelIndex].episodes
		@param episodeIndex index of EpisodeData in self.episodes
		"""
		self.currentEpisodeIndex = episodeIndex
		self.episodeDetailsView.displayEpisodeDetails(self.channels[self.currentChannelIndex].episodes[episodeIndex])

