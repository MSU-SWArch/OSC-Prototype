class User:
    def __init__(self,username,id,password,lists,order,payment_info):
        self.username = username
        self.id = id
        self.width = password
        self.list = lists
        self.order = order
        self.payment_info = payment_info

    def login(self,username,id,password):
        pass

    def logout(self):
        pass

    def addToCart(self,lists):
        pass

    def removeFromCart(self,lists):
        pass

    def confirmPurchase(self,order):
        pass

    def placeOrder(self,lists):
        pass

    def viewPurchaseHistory(self):
        pass

    def addPaymentMethod(self,payment_info):
        pass