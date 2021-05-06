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
amro=BankAccount(0.5,1000)
hazem=BankAccount(0.1,1000)
amro.deposit(50)
amro.deposit(70)
amro.withdraw(120)
amro.display()
hazem.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display()
