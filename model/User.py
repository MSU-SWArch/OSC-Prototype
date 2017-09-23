#!/usr/bin/python
from model.Order import *
from model.Cart import *

class Person:
	def __init__(self, sentName, sentAddress):
		self.name = sentName
		self.address = sentAddress

	def setName(self, newName):
		self.name = newName

	def getName(self):
		return self.name

	def setAddress(self, newAddress):
		self.address = newAddress

	def getAddress(self):
		return self.address


class User(Person):
	def __init__(self, sentName, sentAddress, sentUsername, sentID, sentPassword, sentCartID, sentOrderIDs, sentPaymentInfo):
		Person.__init__(self, sentName, sentAddress)
		self.username = sentUsername
		self.userID = sentID
		self.password = sentPassword
		self.cartID = sentCartID
		self.orderList = sentOrderIDs.split(', ')
		self.paymentInfo = sentPaymentInfo

	def __str__(self):
		tmpOrderStr = ""
		tmpFirstLoop = True
		for curOrder in self.orderList:
			if (not tmpFirstLoop):
				tmpOrderStr += ", "
			tmpOrderStr += curOrder

		return str(str(self.name) + "\\" + str(self.address) + "\\" + str(self.username) + "\\" + str(self.userID) + "\\" + str(self.password) + "\\" + str(self.cartID) + "\\" + str(tmpOrderStr) + "\\" + str(self.paymentInfo))

	def addToCart(self, lists):
		orderList.Cart()
		orderList.addItems(lists)
		pass

	def removeFromCart(self, lists):
		orderList.Cart()
		orderList.removeItems(lists)

	def confirmPurchase(self, order):
		if order == true:
			return true
		else:
			return false
		pass

	def placeOrder(self, items, itemId, sentID):
		orderPlace = Order()
		orderPlace.setItem(items)
		orderPlace.setDate()
		orderPlace.setItemId(itemId)

	def viewPurchaseHistory(self):
		viewHistory=TestDBAccessor

	def addPaymentMethod(self, payment_info, paymentMethod): #paymentMethod is an array, and it'll store all of different payment methods
		self.paymentInfo.append(paymentMethod)
		return paymentMethod
