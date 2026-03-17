"""
Create a class BankAccount with a private attribute __balance.
Add methods deposit() and withdraw() to modify balance.
Show how to access balance safely using a getter.
"""

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance 

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def get_balance(self):
        return self.__balance  


obj = BankAccount(20000)

obj.deposit(10000)
print("Current Balance:", obj.get_balance())

obj.withdraw(5000)
print("Current Balance:", obj.get_balance())