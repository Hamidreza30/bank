class Bank:
    def __init__(self, bank, account_number):
        self.bank = bank
        self.account_number = account_number
        self.balance = 0
        self.history = []

    def transaction(self, sender, receiver, money):
        if sender.balance < money:
            print("The account has no money")

        else:
            sender.balance -= money
            receiver.balance += money
            self.history.append(sender)
            self.history.append(receiver)
            sender.history.append((sender, receiver, money))
            print(f'from:{sender} to:{receiver}  --> {money}$')

    # def balance(self):
    #     print(self.history)
    #
    # def info(self):
    #     print(f'{self.user1.balance},{self.user2.balance},{self.money}')

Bank('Saderat',9899)
Bank('Saderat',9888)
Bank('Saderat',1567)
Bank.transaction(0000,9899,300)
#Bank.check(9899)
