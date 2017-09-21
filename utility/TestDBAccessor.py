#!/usr/bin/python

from model.User import *
from model.Item import *
from model.Order import *
from model.Cart import *

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

	def LoadOrderHistory(self, sentOrderID):
		pass

	def LoadAllData(self):
		self.LoadItemData()
		self.LoadUserData()
		self.LoadCartData()
		self.LoadOrderData()

	def LoadItemData(self):
		del self.itemList[:]
		self.itemFile = open(self.itemFileLoc, 'r').read().split('\n')

		if (self.itemFile[0] != ''):
			for curLine in self.itemFile:
				lineList = curLine.split('\\')
				self.itemList.append(Household(lineList[0], lineList[1], lineList[2], lineList[3], lineList[4], lineList[5]))
			
	def LoadUserData(self):
		self.userDict.clear()

		self.userFile = open(self.userFileLoc, 'r').read().split('\n')
		if (self.userFile[0] != ''):
			for curLine in self.itemFile:
				lineList = curLine.split('\\')
				self.userDict[str(lineList[2])] = User(lineList[0], lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6], lineList[7])
				#print("Test User Import:\nUsers imported:\n\n"self.userDict[str(lineList[2])])

	def LoadCartData(self):
		self.cartFile = open(self.cartFileLoc, 'r')

		self.cartFile.close()

	def LoadOrderData(self):
		self.orderFile = open(self.orderFileLoc, 'r')

		self.orderFile.close()

	# Save Data =============================================

	def SaveItemData(self):
		self.itemFile = open(self.itemFileLoc, 'w')

		self.itemFile.close()

	def SaveUserData(self):
		self.userFile = open(self.userFileLoc, 'w')

		self.userFile.close()

	def SaveCartData(self):
		self.cartFile = open(self.cartFileLoc, 'w')

		self.cartFile.close()

	def SaveOrderData(self):
		self.orderFile = open(self.orderFileLoc, 'w')

		self.orderFile.close()

	def SaveAllData(self):
		self.SaveItemData()
		self.SaveUserData()
		self.SaveCartData()
		self.SaveOrderData()