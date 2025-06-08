'''
Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods 
work as expected.
'''

class BankAccount():
    def __init__(self, balance = 0.0):
        self.balance = balance

    def make_deposit(self):
        amount = float(input("How much would you like to deposit?:> "))
        self.balance += amount
        print(f'Your balance is {self.balance}')

    def make_withdrawal(self):

        amount = float(input("How much would you like to withdraw?:> "))
        if (amount > self.balance):
            print(f"You do not have sufficient balance. Your balance is {self.balance}")
        else:
            self.balance -= amount
            print(f'Withdrawal successful. Your current balance is : {self.balance}')


    def display_balance(self):
        print(f'Your balance is {self.balance}')


my_acc = BankAccount(300)
my_acc.display_balance()
my_acc.make_deposit()
my_acc.make_withdrawal()