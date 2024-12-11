from User import User

class TransactionManager:
    def __init__(self):
        self.users = {}
        self.transactionStarted = False

    def addUser(self, id):
        if id not in self.users:
            newUser = User(id)
            self.users[id] = newUser

    def showAllBalance(self):
        if self.transactionStarted == False:
            print ("No balances")
            return
        
        for _, user in self.users.items():
            user.showPaymentDue()

    def showUserBalance(self, user_id):
        if self.transactionStarted == False:
            print ("No balances")
            return
        self.users[user_id].showPaymentDue()
        self.users[user_id].showReceivables()
    
    def updateBalances(self, receiver, sender_list, amt_list):
        self.transactionStarted = True

        for idx in range(len(sender_list)):
            self.users[receiver].getPaymentFrom(sender_list[idx], amt_list[idx])
            self.users[sender_list[idx]].makePaymentTo(receiver, amt_list[idx])

    def equalExpense(self, receiver, sender_list, total_amt):
        total_amt = total_amt // len(sender_list)
        amt_list = [total_amt] * len(sender_list)
        
        self.updateBalances(receiver, sender_list, amt_list)

    def exactExpense(self, receiver, sender_list, amt_list):
        self.updateBalances(receiver, sender_list, amt_list)

    def percentExpense(self, receiver, sender_list, total_amt, percent_list):
        amt_list = []
        for percent in percent_list:
            amt_list.append(total_amt * (percent / 100))

        self.updateBalances(receiver, sender_list, amt_list)


# tm = TransactionManager()
# tm.addUser('u1')
# tm.addUser('u2')
# tm.addUser('u3')
# tm.addUser('u4')

# tm.showAllBalance()
# tm.showUserBalance('u1')

# tm.equalExpense('u1', ['u2', 'u3', 'u4'], 1000)
# tm.showUserBalance('u4')
# tm.showUserBalance('u1')

# tm.exactExpense('u1', ['u2', 'u3'], [370, 880])
# tm.showAllBalance()

# tm.percentExpense('u4', ['u1', 'u2', 'u3', 'u4'], 1200, [40, 20, 20, 20])
# tm.showUserBalance('u1')
# tm.showAllBalance()



        
