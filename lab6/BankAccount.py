# Author : John Patrick Pitts
# Date   : June 23, 2021
# File   : Lab 6, BackAccount.py

# defines the BankAccount class
class BankAccount:

    # initializes relevant data for the class instance
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

        self.num_deposits = 0
        self.deposit_total = 0
        self.num_withdraws = 0
        self.withdraw_total = 0

    # increments the number of deposits by 1
    def numDeposits(self):
        self.num_deposits += 1

    # increments the number of withdraws by 1
    def numWithdraws(self):
        self.num_withdraws += 1

    # deposits an amount of money in the account, tracking relevant data changes
    def deposit(self, amount):
        self.balance += amount
        self.deposit_total += amount
        self.numDeposits()

    # withdraws an amount of money from the account, tracking relevant data changes
    def withdraw(self, amount):
        self.balance -= amount
        self.withdraw_total += amount
        self.numWithdraws()

    # prints current data on the BankAccount
    def endOfMonth(self):
        print("*" * 10)
        print("Bank account: ", self.name)
        print("Balance: $", self.balance)
        print("Number of deposits: ", self.num_deposits, " totalling $", self.deposit_total)
        print("Number of withdraws: ", self.num_withdraws, " totalling $", self.withdraw_total)
        print("*" * 10)


# main method for this .py file
def main():
    # initializes 2 BankAccount instances
    acct1 = BankAccount(0, "Chase")
    acct2 = BankAccount(100, "Bank of America")

    # implements several deposits and withdraws on the 1st account
    acct1.deposit(50)
    acct1.deposit(50)
    acct1.withdraw(100)
    acct1.withdraw(100)
    acct1.withdraw(100)

    # implements several deposits and withdraws on the 2nd account
    acct2.deposit(25)
    acct2.deposit(25)
    acct2.deposit(5000)
    acct2.withdraw(10)
    acct2.withdraw(1000)
    acct2.withdraw(70)

    # calls the endOfMonth function to report on the accounts
    acct1.endOfMonth()
    acct2.endOfMonth()


# executes the main method if this
if __name__ == "__main__":
    main()
