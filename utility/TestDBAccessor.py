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
		try:
			if (self.userDict[sentUser].password == sentPass):
				print(sentUser + " has logged in!")
				return True
			else:
				return False
		except:
			return False

	def GetCurLogin(self):
		return self.curUser

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

		for curLine in self.itemFile:
			if (curLine != ""):
				lineList = curLine.split('\\')
				if (lineList[0] == "Household"):
					self.itemList.append(Household(lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6]))
				elif (lineList[0] == "Book"):
					self.itemList.append(Book(lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6], lineList[7], lineList[8]))
				elif (lineList[0] == "Toy"):
					self.itemList.append(Toy(lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6]))
				elif (lineList[0] == "Electronic"):
					self.itemList.append(Electronic(lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6]))
				elif (lineList[0] == "Clothes"):
					self.itemList.append(Clothes(lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6], lineList[7]))
				else:
					print("ERROR: Item type not known")

		print("Loaded items:", self.itemList)
			
	def LoadUserData(self):
		self.userDict.clear()
		self.userFile = open(self.userFileLoc, 'r').read().split('\n')

		for curLine in self.userFile:
			if (curLine != ""):
				lineList = curLine.split('\\')
				self.userDict[str(lineList[2])] = User(lineList[0], lineList[1], lineList[2], lineList[3], lineList[4], lineList[5], lineList[6], lineList[7])

	def LoadCartData(self):
		del self.cartList[:]
		self.cartFile = open(self.cartFileLoc, 'r').read().split('\n')

		for curLine in self.cartFile:
			if (curLine != ""):
				lineList = curLine.split('\\')
				itemList = lineList[1].split(", ")
				quantList = lineList[2].split(", ")
				self.cartList.append(Cart(lineList[0], itemList, quantList))

	def LoadOrderData(self):
		self.orderFile = open(self.orderFileLoc, 'r')

		self.orderFile.close()

	# Save Data =============================================

	def SaveItemData(self):
		self.itemFile = open(self.itemFileLoc, 'w')
		for curItem in self.itemList:
			self.itemFile.write(str(curItem) + "\n")
		self.itemFile.close()

	def SaveUserData(self):
		self.userFile = open(self.userFileLoc, 'w')
		for curKey in self.userDict:
			self.userFile.write(str(self.userDict[curKey]) + "\n")
		self.userFile.close()

	def SaveCartData(self):
		self.cartFile = open(self.cartFileLoc, 'w')
		for curCart in self.cartList:
			self.cartFile.write(str(curCart))
		self.cartFile.close()

	def SaveOrderData(self):
		self.orderFile = open(self.orderFileLoc, 'w')

		self.orderFile.close()

	def SaveAllData(self):
		self.SaveItemData()
		self.SaveUserData()
		self.SaveCartData()
		self.SaveOrderData()