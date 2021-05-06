class user:
    def __init__(self,name,age,height,x,y):
        self.name=name
        self.age=age
        self.height=height
        self.balance=[BankAccount(x,y)]
    def newbankaccount(self,x,y):
        self.balance.append(BankAccount(x,y))
    def withdraw(self,amount,banknum):
        self.balance[banknum].withdraw(amount)
    def deposit(self,amount,banknum):
        self.balance[banknum].deposit(amount)
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
        return self.balance
    def yield_interest(self):
        self.balance=self.balance+(self.rate*self.balance)
        return self
amro=user("amro",25,25,25,25)
print(amro.balance[0].display())
