# Bank system

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


acc = SavingsAccount("Rakesh", 1000)

acc.show_balance()
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()
