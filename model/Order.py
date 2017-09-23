#!/usr/bin/python

import datetime
import model.User

class Order():
	def __init__(self, items, itemId, sentID):
		self.transactionDate = now.day
		self.items = items
		self.itemId = itemId

	def setItems(self, items):
		self.items = items

	def setItemId(self, itemId):
		self.itemId = itemID

	def getItems(self, items):
		return self.items
	
	def getTranDate(self):
		return self.transactionDate

	def getItemId(self, itemId):
		return self.itemId