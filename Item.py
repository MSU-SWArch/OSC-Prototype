#!/usr/bin/python

class Item:
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc):
		self.name = sentName
		self.itemId = sentID
		self.price = sentPrice
		self.quantity = sentQuant
		self.description = sentDesc

	def getFeatureDescription():
		return self.description

class Household(Item):
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc, sentType):
		Item.__init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc)
		self.type = sentType

class Book(Item):
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc, sentGenre, sentISBN, sentAuthor):
		Item.__init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc)
		self.genre = sentGenre
		self.isbn = sentISBN
		self.author = sentAuthor

class Toy(Item):
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc, sentType):
		Item.__init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc)
		self.type = sentType

class Electronic(Item):
	def __init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc, sentType):
		Item.__init__(self, sentName, sentID, sentPrice, sentQuant, sentDesc)
		self.type = sentType