#!/usr/bin/python

class Cart:
	def __init__(self, sentCartID, sentItemList, sentQuantList):
		self.cartID = sentCartID
		self.itemList = sentItemList
		self.itemQuantList = sentQuantList

	def __str__(self):
		tmpItemStr = ""
		tmpFirstLoop = True
		for curItem in self.itemList:
			if (not tmpFirstLoop):
				tmpItemStr += ", "
			tmpFirstLoop = False
			tmpItemStr += str(curItem)
		
		tmpQuantStr = ""
		tmpFirstLoop = True
		for curQuant in self.itemQuantList:
			if (not tmpFirstLoop):
				tmpQuantStr += ", "
			tmpFirstLoop = False
			tmpQuantStr += str(curQuant)
		
		return (str(self.cartID) + "\\" + str(tmpItemStr) + "\\" + str(tmpQuantStr))

	def addItems(self, sentItems):
		for curItem in sentItems:
			self.itemList.append(curItem)

	def isEmpty(self):
		if self.items[0] == null:
			return true
		else:
			return false

	def removeItems(self, removalItems):
		for each in self.items:
			if removalItems in self.items:
				self.items.remove(removalItems)

	def getTotalQuantity(self):
		numItems = 0

		for each in self.items:
			numItems += 1

		return numItems

	def getTotalPrice(self, items, price):
		for each in items:
			for each in price:
				price += price
		return price