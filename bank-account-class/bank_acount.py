# FIXME: Add Bank Account class definition here
class BankAccount:
    """A bank account"""
    def __init__(self, beginning_balance = 0):
        self.account_balance = beginning_balance

    def account_deposit(self, deposit_amount):
        self.account_balance += deposit_amount

    def account_withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.account_balance:
            # print("Insufficient funds")
            raise ValueError(f"Invalid transaction: not enough funds to withdraw ${withdrawal_amount}.")
        else:
            self.account_balance -= withdrawal_amount

# You can see how this class should be used below. Make sure you
# run your code and test it out to make sure it works.

account_1 = BankAccount()
account_2 = BankAccount()
account_3 = BankAccount(100)
print(f"account_1 balance is {account_1.account_balance}")
print(f"account_2 balance is {account_2.account_balance}")
print(f"account_3 balance is {account_3.account_balance}")

account_1.account_deposit(100)
account_2.account_deposit(50)
account_3.account_deposit(75)
print(f"account_1 balance is {account_1.account_balance}")
print(f"account_2 balance is {account_2.account_balance}")
print(f"account_3 balance is {account_3.account_balance}")

account_1.account_withdraw(10)
account_2.account_withdraw(10)
account_3.account_withdraw(500)
print(f"account_1 balance is {account_1.account_balance}")
print(f"account_2 balance is {account_2.account_balance}")
print(f"account_3 balance is {account_3.account_balance}")
# account_1.balancecode 
#   >>> 100
# account_2.deposit(50)
# account_2.balance
#   >>> 50
# account_3.deposit(75)
# account_3.balance
#   >>> 175
# account_2.withdraw(10)
# account_2.balance
#   >>> 40
# account_1.withdraw(10)
# account_1.balance
#   >>> 90
# account_2.withdraw(50)
#   >>> "Invalid transaction: not enough funds to withdraw $50." 
# account_2.balance
#   >>> 40    # still 40 since the previous transaction was not successful
