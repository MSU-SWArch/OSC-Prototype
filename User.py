#!/usr/bin/python

class Person:
    def __init__(self, sentName, sentAddress):
        self.name = sentName
        self.address = sentAddress

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setAddress(self, newAddress):
        self.address = newAddress

    def getAddress(self):
        return self.address


class User(Person):
    def __init__(self, sentName, sentAddress, sentUsername, sentID, sentPassword, sentLists, sentOrder, sentPaymentInfo):
        Person.__init__(self, sentName, sentAddress)
        self.username = sentUsername
        self.id = sentID
        self.width = sentPassword
        self.list = sentLists
        self.order = sentOrder
        self.payment_info = sentPaymentInfo

    def login(self, sentUsername, sentID, sentPassword):
        pass

    def logout(self):
        pass

    def addToCart(self, lists):
        pass

    def removeFromCart(self, lists):
        pass

    def confirmPurchase(self, order):
        pass

    def placeOrder(self, lists):
        pass

    def viewPurchaseHistory(self):
        pass

    def addPaymentMethod(self, payment_info):
        pass