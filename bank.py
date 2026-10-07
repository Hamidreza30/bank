class Bank:
    def __init__(self, bank):
        self.bank = bank
        self.accounts = {}
        self.transactions = []

    def transaction(self, sender, receiver, money):
        if sender == "0000":
            if receiver not in self.accounts:
                self.accounts[receiver] = 0

            self.accounts[receiver] += money
            self.transactions.append((sender, receiver, money))
            return True

        if sender not in self.accounts:
            self.accounts[sender] = 0

        if receiver not in self.accounts:
            self.accounts[receiver] = 0

        if self.accounts[sender] < money:
            print("The account has no money")
            return False


        self.accounts[sender] -= money
        self.accounts[receiver] += money
        self.transactions.append((sender, receiver, money))

        return True

    def check(self, account_number):
        if account_number == "0000":
            return -1

        if account_number not in self.accounts:
            return 0

        return self.accounts[account_number]

    def history(self, account_number):
        history = []

        for transaction in self.transactions:
            sender, receiver, money = transaction

            if sender == account_number or receiver == account_number:
                history.append(transaction)

        return history

    def info(self):
        return (
            self.bank,
            len(self.accounts),
            len(self.transactions)
        )

    def save(self):
        with open("bank.txt", "w") as file:
            file.write(self.bank + "\n")

            for account in self.accounts:
                file.write(account + "," + str(self.accounts[account]) + "\n")

            file.write("transactions\n")

            for transaction in self.transactions:
                sender, receiver, money = transaction
                file.write(sender + "," + receiver + "," + str(money) + "\n")

    def load(self):
        with open("bank.txt", "r") as file:
            lines = file.readlines()

        self.bank = lines[0].strip()

        self.accounts = {}

        i = 1

        while lines[i].strip() != "transactions":
            account, money = lines[i].strip().split(",")
            self.accounts[account] = int(money)
            i += 1

        self.transactions = []

        i += 1

        while i < len(lines):
            sender, receiver, money = lines[i].strip().split(",")
            self.transactions.append((sender, receiver, int(money)))
            i += 1


bank = Bank("saderat")
bank.transaction('0000', '3321', 48)
bank.transaction('3321', '1123', 40)
bank.check('3321')
bank.transaction('3321', '1123', 12)
bank.check('1123')
bank.check('0000')
len(bank.history('3321'))
bank.info()
bank.save()
