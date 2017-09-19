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
    def __init__(self, sentName, sentAddress, sentUsername, sentID, sentPassword, sentCartID, sentOrderIDs, sentPaymentInfo):
        Person.__init__(self, sentName, sentAddress)
        self.username = sentUsername
        self.userID = sentID
        self.password = sentPassword
        self.cartID = sentCartID
        self.orderList = sentOrderIDs.split(', ')
        self.paymentInfo = sentPaymentInfo

    def __str__(self):
        return str("User:\nName: " + str(self.name) + "\nAddr: " + str(self.address) + "\nUName: " + str(self.username) + "\nID: " + str(self.userID) + "\nPass: " + str(self.password) + "\nCartID: " + str(self.cartID) + "\nOrderIDs: " + str(self.orderList) + "\nPayment: " + str(self.paymentInfo) + "\n\n")

    def login(self, sentUsername, sentID, sentPassword):
        # Redundent with DBAccessor.verifyLogin()
        pass

    def logout(self):
        # Redundent if logging is managed by DBAccessor
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