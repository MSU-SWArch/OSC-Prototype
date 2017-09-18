#!/usr/bin/python

from User import *
from Item import *
from Order import *
from Cart import *
from TestDBAccessor import *

def main():
	storeRunning = True
	while(storeRunning):
		# Just testing for right now.
		DBReader = DBAccessor("./TestData/testItems.txt", "./TestData/testUsers.txt", "./TestData/testCarts.txt", "./TestData/testOrders.txt")
		DBReader.GetItemData()


		storeRunning = False

main()