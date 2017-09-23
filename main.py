#!/usr/bin/python3

# from model.User import *
# from model.Item import *
# from model.Order import *
# from model.Cart import *
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
	ItemController.PrintAllItems(DBReader)

def AddItem():
	pass

def RemoveItem():
	pass

def PurchaseView():
	pass

def PurchaseHistView():
	pass

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
		print("  3. Add item to cart" + tmpLoginStr)
		print("  4. Remove item from cart" + tmpLoginStr)
		print("  5. Purchase items in cart" + tmpLoginStr)
		print("  6. View purchase history" + tmpLoginStr)
		print("  7. Exit")

		usrInput = input("Operation (1-?): ")
		if (str(usrInput) == "1"):
			LoginScreen()
		elif (str(usrInput) == "2"):
			ItemView()
		elif (str(usrInput) == "3"):
			AddItem()
		elif (str(usrInput) == "4"):
			RemoveItem()
		elif (str(usrInput) == "5"):
			PurchaseView()
		elif (str(usrInput) == "6"):
			PurchaseHistView()
		elif (str(usrInput) == "7"):
			storeRunning = False
		else:
			print("\nThat is not a valid option.\n")

		DBReader.SaveAllData()

main()