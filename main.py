#!/usr/bin/python3

from controller.orderController import *
from controller.userController import *
from controller.itemController import *
from utility.TestDBAccessor import *

def LoginScreen():
	if (DBReader.curUser != ""):
		DBReader.curUser = ""
		print("\nYou are now logged out.\n")
	else:
		unameInput = input("\nUsername: ")
		passInput = input("Password: ")
		DBReader.VerifyLogin(unameInput, passInput)
		print()

def ItemView():
	print()
	ItemController.PrintAllItems(DBReader)
	print()

def AddItem():
	if (DBReader.curUser == ""):
		print("\nYou need to log in to add items!\n")
		return

	usrInput = input("What item would you like to add?\n")
	itemName = DBReader.GetItemName(usrInput)
	if (itemName == "Null"):
		print("That is not a valid item name.")
		return
	usrInput = input("How many would you like to add?\n")
	DBReader.AddItem(str(itemName), int(usrInput))

def RemoveItem():
	if (DBReader.curUser == ""):
		print("\nYou need to log in to add items!\n")
		return

	usrInput = input("What item would you like to remove?\n")
	itemName = DBReader.GetItemName(usrInput)
	if (itemName == "Null"):
		print("That is not a valid item name.")
		return
	usrInput = input("How many would you like to remove?\n")
	DBReader.RemoveItem(str(itemName), int(usrInput))

def PurchaseView():
	if (DBReader.curUser == ""):
		print("\nYou need to log in to add items!\n")
		return

	DBReader.PurchaseCart("./TestData/testPastOrders.txt")

def PurchaseHistView():
	print("\n")
	print(open("./TestData/testPastOrders.txt", 'r').read())

def ViewCart():
	DBReader.PrintCart()

def main():
	storeRunning = True
	usrInput = ""
	global DBReader

	# Just testing for right now.
	DBReader = DBAccessor("./TestData/testItems.txt", "./TestData/testUsers.txt", "./TestData/testCarts.txt", "./TestData/testOrders.txt")
	DBReader.LoadAllData()

	while(storeRunning):
		tmpLoginStr = ""
		if (DBReader.curUser == ""):
			tmpLoginStr = " (Requires login)"
		print("Operations:")
		if (DBReader.curUser == ""):
			print("  1. Log in")
		else:
			print("  1. Log out")
		print("  2. View Items")
		print("  3. View Cart")
		print("  4. Add item to cart" + tmpLoginStr)
		print("  5. Remove item from cart" + tmpLoginStr)
		print("  6. Purchase items in cart" + tmpLoginStr)
		print("  7. View purchase history" + tmpLoginStr)
		print("  8. Exit")

		usrInput = input("Operation (1-8): ")
		if (str(usrInput) == "1"):
			LoginScreen()
		elif (str(usrInput) == "2"):
			ItemView()
		elif (str(usrInput) == "3"):
			ViewCart()
		elif (str(usrInput) == "4"):
			AddItem()
		elif (str(usrInput) == "5"):
			RemoveItem()
		elif (str(usrInput) == "6"):
			PurchaseView()
		elif (str(usrInput) == "7"):
			PurchaseHistView()
		elif (str(usrInput) == "8"):
			storeRunning = False
		else:
			print("\nThat is not a valid option.\n")

		DBReader.SaveAllData()

main()