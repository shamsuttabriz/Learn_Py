class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f'This money is not for you! Minimum withdraw {self.min_withdraw}'
        elif amount > self.max_withdraw:
            return f'You crossed maximum limit! Maximum withdraw {self.max_withdraw}' 
        elif amount > self.balance:
            return 'You wont fall apart. There is no money for you.'
        else:
            self.balance = self.balance - amount
            return f'After withdraw your balance: {self.balance}'
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return f'After deposit your balance: {self.balance}'
    
my_balance = Bank(5000)
after_withdraw = my_balance.withdraw(4)
print(after_withdraw) # This money is not for you! Minimum withdraw 100
after_withdraw = my_balance.withdraw(40000)
print(after_withdraw) # You crossed maximum limit! Maximum withdraw 10000
after_withdraw = my_balance.withdraw(9000)
print(after_withdraw) # You wont fall apart. There is no money for you.
after_withdraw = my_balance.withdraw(4000)
print(after_withdraw) # After withdraw your balance: 1000
after_deposit = my_balance.deposit(4322)
print(after_deposit) # After deposit your balance: 5322
