#!/usr/bin/python

from User import *
from Item import *
from Order import *
from Cart import *
from utility/TestDBAccessor import *

def main():
	storeRunning = True

	# Just testing for right now.
	DBReader = DBAccessor("./TestData/testItems.txt", "./TestData/testUsers.txt", "./TestData/testCarts.txt", "./TestData/testOrders.txt")
	DBReader.GetUserData()
	DBReader.GetItemData()

	while(storeRunning):
		print("Operations:")
		if (DBReader.curUser != ""):
			print("  1. Log in")
		else:
			print("  1. Log out")
			print("  2. View Items")
		


		storeRunning = False

main()