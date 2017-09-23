#!/usr/bin/python

import datetime

class Order():
	def __init__(self, sentOrderID, sentItemList, sentQuantList, sentPriceList, sentDateTime):
		self.orderID = sentOrderID
		self.itemList = sentItemList
		self.itemQuantList = sentQuantList
		self.priceList = sentPriceList
		self.transactionDate = sentDateTime

	def __str__():
		tmpItemStr = ""
		for i in range(0, (len(self.itemList) - 1)):
			tmpItemStr += (str(self.itemList[i]) + "\t(" + str(self.quantList[i]) + ")\t$" + (self.priceList[i] * self.quantList[i]) + "\n")
		tmpItemStr += "\n"

		return str("Order ID: " + str(self.orderID) + "Date: " + str(self.transactionDate) + "\nItems:\n" + str(tmpItemStr))

	def setItems(self, sentItemList):
		self.itemList = sentItemList

	def getItems(self, items):
		return self.itemList
	
	def getTranDate(self):
		return self.transactionDate