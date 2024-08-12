# Author: Tahjae Jackson
# Date: October 19, 2021
# Purpose:

# Create a class file that represents a bank account.
# -Your class should have 3 instance variables: balance(integer), Account_Type(string), overdraft(boolean)
# -Account type is a string describing an account: an account is "savings" or "checkings"
# -Overdraft is True is balance < 0, otherwise False. Overdraft only allowed for checking accounts
# -Your class should have 4 methods:
#     1. __init__(self,...) takes an initial deposit and string type as parameters
#     2. withdraw(self,...) takes an integer amount as parameter. RETURNS True if successful, False otherwise
#     3. deposit(self,...) takes integer amount and adds to account balance:
#        if balance>=0, overdraft is set to False
#     4. __str__(self): when called, should RETURN a string with type, balance, and overdraft status of account, 100, False


class Bank_account:
    def __init__(self, initial_dep, type):
        self.balance = initial_dep
        self.account_type = type
        self.overdraft = False

    def withdraw(self, amount):
        if amount > self.balance and self.account_type == "savings":
            print("You do not have enough funds for this withdrawal")
            return False

        elif amount > self.balance and self.account_type == "checkings":
            self.overdraft = True

        self.balance = self.balance - amount
        return True

    def deposit(self,dep):
        self.balance = self.balance + dep
        if self.balance >= 0:
            self.overdraft = False


    def __str__(self):
        return (str(self.account_type)+", "+str(self.balance)+", "+str(self.overdraft))

