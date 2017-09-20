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
		self.userDict = {}
		self.cartList = []
		self.orderList = []

		self.curUser = ""

	def VerifyLogin(self, sentUser, sentPass):
		for curUser in self.userList:
			#if curUser.
			pass
		return False

	def AddUser(self, sentUsername, sentPassword):
		pass

	def GetOrderHistory(self, sentOrderID):
		pass

	def GetAllData(self):
		GetItemData(self)
		GetUserData(self)
		GetCartData(self)
		GetOrderData(self)

	def GetItemData(self):
		del self.itemList[:]
		self.itemFile = open(self.itemFileLoc, 'r').read().split('\n')
		for curLine in self.itemFile:
			lineList = curLine.split('\\')
			self.itemList.append(Household(lineList[0], lineList[1], lineList[2], lineList[3], lineList[4], lineList[5]))
			
	def GetUserData(self):
		self.userDict.clear()
		self.itemFile = open(self.userFileLoc, 'r').read().split('\n')
		for curLine in self.itemFile:
			lineList = curLine.split('\\')
			self.userDict[str(lineList[2])] = User(lineList[0], lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6], lineList[7])
			#print("Test User Import:\nUsers imported:\n\n"self.userDict[str(lineList[2])])

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