#!/usr/bin/python

class Item:
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc):
		self.name = sentName
		self.itemID = sentID
		self.price = sentPrice
		self.quantity = sentQuant
		self.description = sentDesc

	def __str__(self):
		return (str(self.name) + "\\" + str(self.itemID) + "\\" + str(self.price) + "\\" + str(self.quantity) + "\\" + str(self.description))

	def getFeatureDescription():
		return self.description

class Household(Item):
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc, sentType):
		super(Household, self).__init__(sentName, sentID, sentPrice, sentQuant, sentDesc)
		self.itemType = sentType

	def __str__(self):
		return ("Household\\" + str(Item.__str__(self)) + "\\" + str(self.itemType))


class Book(Item):
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc, sentGenre, sentISBN, sentAuthor):
		Item.__init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc)
		self.genre = sentGenre
		self.isbn = sentISBN
		self.author = sentAuthor

	def __str__(self):
		return ("Book\\" + str(Item.__str__(self)) + "\\" + str(self.genre) + "\\" + str(self.isbn) + "\\" + str(self.author))

class Toy(Item):
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc, sentType):
		Item.__init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc)
		self.itemType = sentType

	def __str__(self):
		return ("Toy\\" + str(Item.__str__(self)) + "\\" + str(self.itemType))

class Electronic(Item):
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc, sentType):
		Item.__init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc)
		self.itemType = sentType

	def __str__(self):
		return ("Electronic\\" + str(Item.__str__(self)) + "\\" + str(self.itemType))

class Clothes(Item):
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc, sentGender, sentSection):
		Item.__init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc)
		self.gender = sentGender
		self.section = sentSection

	def __str__(self):
		return ("Clothes\\" + str(Item.__str__(self)) + "\\" + str(self.gender) + "\\" + str(self.section))