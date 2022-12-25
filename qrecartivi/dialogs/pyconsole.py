#!/usr/bin/env python
#-*- coding:utf-8 -*-

from gevent import monkey; monkey.patch_all()

import gevent

from PyQt5.QtWidgets import QPlainTextEdit, QLineEdit, QPushButton, QDialogButtonBox
from PyQt5.QtCore import QTimer, QMetaObject, Qt

from pyqtconsole.console import PythonConsole

from SimpleQt import Dialog, VBox, HBox

class PythonConsoleDialog(Dialog):
	def __init__(self):
		Dialog.__init__(self, title="Python console", buttons=QDialogButtonBox.Close)
		
		self.console = PythonConsole()
		self.addWidget(self.console)

		self.console.eval_executor(gevent.spawn)
		
		self._eventTimer = QTimer()
		self._eventTimer.timeout.connect(self.process_events)
		self._eventTimer.start(0)
		
		self.buttonBox.button(QDialogButtonBox.Close).setAutoDefault(False)

	def process_events(self):
		# Cooperative yield, allow gevent to monitor file handles via libevent
		gevent.sleep(0.01)

