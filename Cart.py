#!/usr/bin/python
import rand

class Cart:
	def __init__(self, items, cartId,):
		self.items = items
		self.cartId = rand()e


	def addItems(newitems):
		for each in newitems:
			self.items.append(newitems)

		return true

	def isEmpty():
		if self.items[0] == null:
			return true
		else:
			return false

	def removeItems(removalItems):

		for each in self.items:
			if removalItems in self.items:
				self.items.remove(removalItems)
				
		return true

	def getTotalQuantity(self):
		numItems = 0

		for each in self.items:
			numItems += 1

		return numItems

	def getTotalPrice(items, price):
		for each in items:
			for each in price:
				price += price
		return price

		return


