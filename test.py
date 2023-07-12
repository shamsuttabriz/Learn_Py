class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.minimum_withdraw = 100
        self.maximum_withdraw = 10000
    
    def withdraw(self, amount):
        if amount < self.minimum_withdraw:
            return f'No Money for you! Please minimum withdraw: {self.minimum_withdraw}'
        elif amount > self.maximum_withdraw:
            return f'No Money for you! You daily withdraw limit: {self.maximum_withdraw}'
        elif amount > self.balance:
            return 'Insufficient Balance in your bank'
        else:
            self.balance -= amount
            return f'Here your money is: {amount}'
        
    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
        

my_bank = Bank(9000)
x = my_bank.withdraw(5)
print(x)
print(f'Your present balance: {my_bank.balance}')

x = my_bank.withdraw(50000)
print(x)
print(f'Your present balance: {my_bank.balance}')

x = my_bank.withdraw(9500)
print(x)
print(f'Your present balance: {my_bank.balance}')

x = my_bank.withdraw(4000)
print(x)
print(f'Your present balance: {my_bank.balance}')

my_bank.deposit(5009)
print(f'Your present balnce: {my_bank.balance}')


