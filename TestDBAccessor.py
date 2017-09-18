#!/usr/bin/python

from User import *
from Item import *
from Order import *
from Cart import *

class DBAccessor():
	def __init__(self, sentItemFileLoc, sentUserFileLoc, sentCartFileLoc, sentOrderFileLoc):
		self.itemFileLoc = sentItemFileLoc
		self.userFileLoc = sentUserFileLoc
		self.cartFileLoc = sentCartFileLoc
		self.orderFileLoc = sentOrderFileLoc

		self.itemList = []
		self.userList = []
		self.cartList = []
		self.orderList = []

	def VerifyLogin(self, sentUser, sentPass):
		for curUser in self.userList:
			if curUser.
		return False

	def GetAllData(self):
		GetItemData(self)
		GetUserData(self)
		GetCartData(self)
		GetOrderData(self)

	def GetItemData(self):
		self.itemFile = open(self.itemFileLoc, 'r').read().split('\n')
		i = 0
		for curLine in self.itemFile:
			lineList = curLine.split('\ ')
			userList[i] = User(lineList[0], lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6], lineList[7])
			

	def GetUserData(self):
		self.userFile = open(self.userFileLoc, 'r')

		self.userFile.close()

	def GetCartData(self):
		self.cartFile = open(self.cartFileLoc, 'r')

		self.cartFile.close()

	def GetOrderData(self):
		self.orderFile = open(self.orderFileLoc, 'r')

		self.orderFile.close()

	# SET Data =============================================

	def SetAllData(self):
		SetItemData(self)
		SetUserData(self)
		SetCartData(self)
		SetOrderData(self)

	def SetItemData(self):
		self.itemFile = open(self.itemFileLoc, 'w')

		self.itemFile.close()

	def SetUserData(self):
		self.userFile = open(self.userFileLoc, 'w')

		self.userFile.close()

	def SetCartData(self):
		self.cartFile = open(self.cartFileLoc, 'w')

		self.cartFile.close()

	def SetOrderData(self):
		self.orderFile = open(self.orderFileLoc, 'w')

		self.orderFile.close()