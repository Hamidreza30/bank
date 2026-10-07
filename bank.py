import random


class Bank:
    def __init__(self, bank):
        self.bank = bank
        self.accounts = {}
        self.transactions = []

    def register(self, name, age):
        account_number = str(random.randint(1000, 9999))

        while account_number in self.accounts:
            account_number = str(random.randint(1000, 9999))

        self.accounts[account_number] = {
            "name": name,
            "age": age,
            "balance": 0
        }

        print("Registration successful!")
        print(f"Your account number is: {account_number}")

        self.save()

        return account_number

    def transaction(self, sender, receiver, money):

        if sender == "0000":

            if receiver not in self.accounts:
                print("Receiver account does not exist")
                return False

            self.accounts[receiver]["balance"] += money

            self.transactions.append(
                (sender, receiver, money)
            )

            self.save()

            return True

        if sender not in self.accounts:
            print("Sender account does not exist")
            return False

        if receiver not in self.accounts:
            print("Receiver account does not exist")
            return False

        if self.accounts[sender]["balance"] < money:
            print("The account has no money")
            return False

        self.accounts[sender]["balance"] -= money
        self.accounts[receiver]["balance"] += money

        self.transactions.append(
            (sender, receiver, money)
        )

        self.save()

        return True

    def balance_of(self, account_number):

        if account_number == "0000":
            return -1

        if account_number not in self.accounts:
            return 0

        return self.accounts[account_number]["balance"]

    def history(self, account_number):

        history = []

        for transaction in self.transactions:

            sender, receiver, money = transaction

            if sender == account_number or receiver == account_number:
                history.append(transaction)

        return history

    def save(self):

        with open("bank.txt", "w") as file:

            file.write(self.bank + "\n")

            file.write("accounts\n")

            for account in self.accounts:

                name = self.accounts[account]["name"]
                age = self.accounts[account]["age"]
                balance = self.accounts[account]["balance"]

                file.write(
                    account + "," +
                    name + "," +
                    str(age) + "," +
                    str(balance) + "\n"
                )

            file.write("transactions\n")

            for transaction in self.transactions:

                sender, receiver, money = transaction

                file.write(
                    sender + "," +
                    receiver + "," +
                    str(money) + "\n"
                )

    def load(self):

        with open("bank.txt", "r") as file:
            lines = file.readlines()

        self.bank = lines[0].strip()

        self.accounts = {}

        i = 2

        while i < len(lines) and lines[i].strip() != "transactions":

            account, name, age, balance = lines[i].strip().split(",")

            self.accounts[account] = {
                "name": name,
                "age": int(age),
                "balance": int(balance)
            }

            i += 1

        self.transactions = []

        i += 1

        while i < len(lines):

            sender, receiver, money = lines[i].strip().split(",")

            self.transactions.append(
                (sender, receiver, int(money))
            )

            i += 1


bank = Bank("saderat")

bank.load()

print(bank.accounts)
print(bank.transactions)
