# Putting all the lessons we have learnt from classes and objects together,
# we will create a project that will help us understand the concepts better.

# Project description:
# We will create a simple banking system that will allow us to create bank accounts,
# deposit money into the accounts, withdraw money from the accounts, and check the balance of the accounts.
# We will create a class called Account that will serve as a template for other classes to inherit from.

# The Account class will have the following properties:
# 1. account_number - This will be a unique number that will be assigned to each account.
# 2. account_type - This will be the type of account. It can be either savings or current.
# 3. balance - This will be the amount of money in the account.
# 4. account_holder - This will be the name of the person that owns the account.

# The Account class will have the following methods:
# 1. deposit(amount) - This method will be used to deposit money into the account.
# 2. withdraw(amount) - This method will be used to withdraw money from the account.
# 3. get_balance() - This method will be used to check the balance of the account.
# 4. get_account_number() - This method will be used to get the account number of the account.
# 5. get_account_type() - This method will be used to get the account type of the account.
# 6. get_account_details() - This method will be used to get the account details of the account.

# We will create two classes called SavingsAccount and CurrentAccount that will inherit from the Account class.
# The SavingsAccount class will have the following methods:
# 2. get_account_details() - This method will override the get_account_details() method in the Account class.

# The CurrentAccount class will have the following methods:
# 2. get_account_details() - This method will override the get_account_details() method in the Account class.


class Account:
    def __init__(self, account_number, account_type, balance, account_holder):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("You do not have enough money!!! Thief")

        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def get_account_type(self):
        return self.account_type

    def get_account_details(self):
        return {
            "Account Name": self.account_holder,
            "Account Type": self.account_type,
            "Account Number": self.account_number,
            "Account Balance": self.balance,
        }


class SavingsAccount(Account):
    def get_account_details(self):
        return {
            "Account Name": self.account_holder,
            "Account Type": self.account_type,
            "Account Number": self.account_number,
            "Account Balance": self.balance,
            "Extra Details": "This is an account for students",
        }


class CurrentAccount(Account):
    def get_account_details(self):
        return {
            "Account Name": self.account_holder,
            "Account Type": self.account_type,
            "Account Number": self.account_number,
            "Account Balance": self.balance,
            "Extra Details": "This is an account for businesses",
        }


john = SavingsAccount(129762, "Savings", 200, "John Yemi")

# print(john.get_balance())

# john.deposit(200000)
# john.deposit(3000)
# john.deposit(1000)


# print(john.get_balance())

# john.withdraw(4200)

# print(john.get_balance())


mary = CurrentAccount(9988732, "Current", 60000, "Mary King")
print(mary.get_balance())
print(mary.get_account_details())
