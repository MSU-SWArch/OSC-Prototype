#!/usr/bin/python

import datetime
import User

class Order(User):
	def __init__(self,items, itemId, sentID):
		self.transactionDate = now.day
		self.items = items
		self.itemId = itemId

	def getItems(self, items):
		return self.items
	
	def getTranDate(self):
		return self.transactionDate

	def getItemId(self, itemId):
		return self.itemId

	pass