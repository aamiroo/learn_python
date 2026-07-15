"""A bank account in Python using a class
Displays account information.
You can add to or withdraw from the deposit.
"""
import sys

class Bank:

    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance
    def show(self):
        print ("owner account: " , self.owner)
        print ("Capital amount: " , self.balance)
    def deposit(self, amount):
        self.balance += amount
    def withdraw (self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")
account1 = Bank("ali" , 5000)

Action = input("What process do you want? \n1.View account information  \n2.Add to deposit \n3.Deducting from the deposit\n" )
while True:
    if Action.isdigit():
        Action = int (Action)
    if Action == "q" :
        sys.exit()
    if Action == 1:
        account1.show()
    elif Action == 2:
        account1.deposit(int(input("Enter the amount:")))
        account1.show()
    elif Action == 3:
        account1.withdraw(int(input("Enter the amount:")))
        account1.show()
    
    