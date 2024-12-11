from TransactionManager import TransactionManager


user_input = '''SHOW
SHOW u1
EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
SHOW u4
SHOW u1
EXPENSE u1 1250 2 u2 u3 EXACT 370 880
SHOW
EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20
SHOW u1
SHOW'''

def main():
    commands = user_input.split("\n")

    tm = TransactionManager()
    for command in commands:
        word_list = command.split()

        if word_list[0] == 'SHOW':
            if len(word_list) == 1:
                tm.showAllBalance()
            else:
                user_id = word_list[1]
                tm.addUser(user_id)
                tm.showUserBalance(user_id)
        else:
            receiver, total_amount, sender_count = word_list[1], int(word_list[2]), int(word_list[3])
            sender_list = word_list[4: 4 + sender_count]
            split_list = list(map(int,word_list[4 + sender_count + 1:]))

            tm.addUser(receiver)
            for sender in sender_list:
                tm.addUser(sender)

            if 'EQUAL' in word_list:
                tm.equalExpense(receiver, sender_list, total_amount)
            elif 'EXACT' in word_list:
                tm.exactExpense(receiver, sender_list, split_list)
            else:
                tm.percentExpense(receiver, sender_list, total_amount, split_list)

if __name__=="__main__":
    main()