#!/usr/bin/python

class ItemController():
	def PrintAllItems(DBReader):
		itemVarList = []
		print("\nCurrent item(s) inventory:\n")
		for curItem in DBReader.itemList:
			# print(str(curItem.name) + ":")
			# print("Price: " + str(curItem.price))
			# print("Quantity: " + str(curItem.quantity))
			del itemVarList[:]
			itemVarList = str(curItem).split("\\")

			print(str(curItem.name) + ":")
			print("Price: " + str(curItem.price))
			print("Item ID: " + str(curItem.itemID))
			print("Quantity: " + str(curItem.quantity))
			if ((itemVarList[0] == "Household") or (itemVarList[0] == "Toy") or (itemVarList[0] == "Electronic")):
				print("Type: " + curItem.itemType)
			elif (itemVarList[0] == "Book"):
				print("Genre: " + curItem.genre)
				print("ISBN: " + curItem.isbn)
				print("Author: " + curItem.author)
			elif (itemVarList[0] == "Clothes"):
				print("Gender: " + curItem.gender)
				print("Section: " + curItem.section)
			print(curItem.description + "\n")