import random
import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age =int(age)
        self.account_number = str(random.randint(999, 9999))

    def __str__(self):
        return f"name:{self.name}, age:{self.age} , account_number:{self.account_number} "

#____________________________________________

class Transaction:

    def __init__(self, sender, receiver, money):
        self.sender = sender
        self.receiver = receiver
        self.money = int(money)
        self.datetime = datetime.datetime.now()

    def __str__(self):
        return (
            f"Sender: {self.sender}\n"
            f"Receiver: {self.receiver}\n"
            f"Money: {self.money}\n"
            f"Datetime: {self.datetime}"
        )
#_________________________________________

class Bank:
    def __init__(self, name):
        self.name = name
        self.transact = []
        self.accounts = []

    def sign_up(self, name, age):
        user = User(name, age)

        account = {
            "account_number": user.account_number,
            "name": user.name,
            "age": user.age,
            "balance": 0
        }

        self.accounts.append(account)
        return account

    def transaction(self, sender_number, receiver_number, money):

        if sender_number == '0000':
            receiver = self.get_user_by_account_number(receiver_number)

            if receiver is None:
                print("Receiver account does not exist")
                return False

            if money <= 0:
                print("Money must be greater than zero")
                return False

            receiver["balance"] += money
            transaction = Transaction(sender_number, receiver_number, money)
            self.transact.append(transaction)
            return True

        sender = self.get_user_by_account_number(sender_number)
        receiver = self.get_user_by_account_number(receiver_number)

        if sender is None:
            print("Sender account does not exist")
            return False

        if receiver is None:
            print("Receiver account does not exist")
            return False

        if money <= 0:
            print("Money must be greater than zero")
            return False

        if sender["balance"] < money:
            print("Sender account balance less than money")
            return False

        sender["balance"] -= money
        receiver["balance"] += money

        transaction = Transaction(sender_number, receiver_number, money)
        self.transact.append(transaction)
        return True



    def get_user_by_account_number(self, account_number):
        for account in self.accounts:
            if account["account_number"] == account_number:
                return account
        return None

    def balance(self, account_number):
        if account_number == "0000":
            return -1

        account = self.get_user_by_account_number(account_number)

        if account is not None:
            return account["balance"]

        return False



    def save(self):
        with open('bank.txt', "w", encoding="utf-8") as file:
            file.write(self.name + "\n")

            for account in self.accounts:
                file.write(
                    f'{account["account_number"]},'
                    f'{account["name"]},'
                    f'{account["age"]},'
                    f'{account["balance"]}\n'
                )

        return "Data saved successfully!"


    def load(self):
        file = open("bank.txt", "r")

        lines = file.readlines()

        file.close()

        self.name = lines[0].strip()
        self.accounts = []

        for line in lines[1:]:
            account_number, name, age, balance = line.strip().split(",")

            account = {
                "account_number": account_number,
                "name": name,
                "age": int(age),
                "balance": int(balance)
            }

            self.accounts.append(account)

# bank=Bank('Saman')
#
# user1=User('ali',50)
# user2=User('neda',19)
# user3=User('mahdi',30)
#
# bank.sign_up(user1.name, user1.age)
# bank.sign_up(user2.name, user2.age)
# bank.sign_up(user3.name, user3.age)
#
# print(user1.account_number)
# print(user2.account_number)
# print(user3.account_number)
#
# bank.save()

# bank=Bank('Saman')
# bank.load()
# print(bank.accounts)
# bank.transaction('8868','4097',100)
# bank.transaction('8868','2913',100)
#Transaction('8868','4097',100)






