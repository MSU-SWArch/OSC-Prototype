#!/usr/bin/python

from model.User import *
from model.Item import *
from model.Order import *
from model.Cart import *
import random

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

	def PrintCart(self):
		if (self.curUser == ""):
			print("You need to log in to do that!\n")
			return

		cartFound = False
		for curCart in self.cartList:
			if (str(curCart.cartID) == str(self.userDict[self.curUser].cartID)):
				cartFound = True
				cartVars = str(curCart).split("\\")
				cartItemList = cartVars[1].split(", ")
				cartQuantList = cartVars[2].split(", ")
				totalPrice = 0.0
				print("\nItems in cart:")
				for i in range(0, len(cartItemList)):
					curItemPrice = 0.0
					for curItem in self.itemList:
						if str(curItem.name).upper() == str(cartItemList[i]).upper():
							curItemPrice = curItem.price
					totalPrice += (float(curItemPrice) * int(cartQuantList[i]))
					print(str(cartItemList[i]) + "\t" + cartQuantList[i] + "\t$" + str(float(curItemPrice) * int(cartQuantList[i])))
				print("Total: $" + str(totalPrice) + "\n")

		if (not cartFound):
			print("You don't have anything in your cart!")

	def GetItemName(self, sentItemName):
		for curItem in self.itemList:
			if (str(sentItemName).upper() == str(curItem.name).upper()):
				return str(curItem.name)

		return "Null"

	def AddItem(self, sentItemName, sentQuant):
		for curItem in self.itemList:
			if (str(sentItemName).upper() == str(curItem.name).upper()):
				if (int(sentQuant) > int(curItem.quantity)):
					sentQuant = curItem.quantity
					curItem.quantity = 0
					print("There aren't that many! Adding " + str(sentQuant) + ".")
				else:
					curItem.quantity = int(curItem.quantity) - int(sentQuant)

		cartFound = False
		for curCart in self.cartList:
			if (str(curCart.cartID) == str(self.userDict[self.curUser].cartID)):
				cartFound = True
				curCart.itemList.append(sentItemName)
				curCart.itemQuantList.append(sentQuant)
		if (not cartFound):
			self.userDict[self.curUser].cartID = int(random.random() * 9999)
			self.cartList.append(Cart(self.userDict[self.curUser].cartID, [sentItemName], [sentQuant]))

		print(str(sentQuant) + " " + str(sentItemName) + " has been added to cart" + str(self.userDict[self.curUser].cartID))

	def RemoveItem(self, sentItemName, sentQuant):
		itemFound = False
		for curCart in self.cartList:
			if (str(curCart.cartID) == str(self.userDict[self.curUser].cartID)):

				for curItem in curCart.itemList:
					if (str(curItem).upper() == str(sentItemName).upper()):
						itemFound = True
						itemInd = curCart.itemList.index(curItem)
					curCart.itemQuantList[itemInd] = int(curCart.itemQuantList[itemInd]) - int(sentQuant)
					if (curCart.itemQuantList[itemInd] <= 0):
						sentQuant += curCart.itemQuantList[itemInd]
						del curCart.itemList[itemInd]
						del curCart.itemQuantList[itemInd]

		if (not itemFound):
			print("You don't have any of that item in your cart.\n")
		else:
			for curItem in self.itemList:
				if (str(sentItemName).upper() == str(curItem.name).upper()):
					curItem.quantity = int(curItem.quantity) + int(sentQuant)
			print("Item removed.")

	def PurchaseCart(self, sentFileLoc):
		print("Items in your current cart:\n")
		self.PrintCart()
		usrInput = input("Would you like to purchase these items now (y/n)? ")

		if (str(usrInput).upper() != "Y"):
			print("\nCancelling order.\n")
			return

		print("\nCurrent shipment information:\n")
		print("Name: " + str(self.userDict[self.curUser].name))
		print("Address: " + str(self.userDict[self.curUser].address))
		print("Card info: " + str(self.userDict[self.curUser].paymentInfo))
		usrInput = input("\nIs all of this correct (y/n)? ")
		if (str(usrInput).upper() != "Y"):
			print("\nPlease enter the correct information.\n")
			self.userDict[self.curUser].name = input("Name: ")
			self.userDict[self.curUser].address = input("Address: ")
			self.userDict[self.curUser].paymentInfo = input("Card info: ")

		for curCart in self.cartList:
			if (str(curCart.cartID) == str(self.userDict[self.curUser].cartID)):
				self.orderFile = open(sentFileLoc, 'a')
				self.orderFile.write("ID: " + str(curCart.cartID) + "\n")
				tmpTotPrice = 0.0
				for i in range(0, len(curCart.itemList)):
					for curItem in self.itemList:
						if str(curItem.name).upper() == str(curCart.itemList[i]).upper():
							tmpPrice = float(curItem.price) * int(curCart.itemQuantList[i])
					tmpTotPrice += tmpPrice
					self.orderFile.write(str(curCart.itemList[i]) + "\t" + str(curCart.itemQuantList[i]) + "\t$" + str(tmpPrice) + "\n")
				self.orderFile.write("Total: $" + str(tmpTotPrice) + "\n\n")
				self.orderFile.close()

				del curCart
				self.userDict[self.curUser].cartID = ""

		print("Your order has now been shipped!")


	def VerifyLogin(self, sentUser, sentPass):
		try:
			if (self.userDict[sentUser].password == sentPass):
				self.curUser = sentUser
				print(sentUser + " has logged in!")
				return True
			else:
				return False
		except:
			print("Login failed.")
			return False

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
			self.cartFile.write(str(curCart) + "\n")
		self.cartFile.close()

	def SaveOrderData(self):
		self.orderFile = open(self.orderFileLoc, 'w')

		self.orderFile.close()

	def SaveAllData(self):
		self.SaveItemData()
		self.SaveUserData()
		self.SaveCartData()
		self.SaveOrderData()