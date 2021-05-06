class user:
    def __init__(self,name,age,height,x,y):
        self.name=name
        self.age=age
        self.height=height
        self.balance=BankAccount(x,y)
    def deposit(self,amount):
        self.balance.deposit(amount)
    def withdraw(self,amount):
        self.balance.withdraw(amount)
    def display(self):
        self.balance.display
class BankAccount:
    def __init__(self,rate,balance):
        self.balance=balance
        self.rate=rate
    def deposit(self,amount):
        self.balance+=amount
        return self
    def withdraw(self,amount):
        self.balance-=amount
        return self
    def display(self):
        print(self.balance)
    def yield_interest(self):
        self.balance=self.balance+(self.rate*self.balance)
        return self
 