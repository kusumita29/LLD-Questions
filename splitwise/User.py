from numpy import rec

def print_statement(sender, receiver, amt):
    print (f'User{sender[1:]} owes User{receiver[1:]}: {amt}')

class User(object):
    def __init__(self, id):
        self.id = id
        self.balanceSheet = {}

    def showPaymentDue(self):
        for receiver_id, amt in self.balanceSheet.items():
            if amt > 0:
                print_statement(self.id, receiver_id, amt)

    def showReceivables(self):
        for sender_id, amt in self.balanceSheet.items():
            if amt < 0:
                print_statement(sender_id, self.id, -amt)

    def getName(self):
        return self.name
    
    def makePaymentTo(self, receiver_id, amt):
        if receiver_id not in self.balanceSheet:
            self.balanceSheet[receiver_id] = 0
        self.balanceSheet[receiver_id] += amt

    def getPaymentFrom(self, sender_id, amt):
        if sender_id not in self.balanceSheet:
            self.balanceSheet[sender_id] = 0
        self.balanceSheet[sender_id] -= amt
