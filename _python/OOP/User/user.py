class user:
    def __init__(self,name,age,height,cash):
        self.name=name
        self.age=age
        self.height=height
        self.cash=cash
    def make_withdrawal(self, amount):
        self.cash-=amount
    def make_deposit(self, amount):
        self.cash+=amount
    def display_user_balance(self):
        return self.cash
    def transfer_money(self, other_user, amount):
        self.cash-=amount
        other_user.make_deposit(amount)
amro=user("amro",22,15,250)
mohammad=user("mohammad",23,13,500)
suad=user("suad",50,10,600)
amro.make_deposit(200)
amro.make_deposit(100)
amro.make_deposit(500)
amro.make_withdrawal(700)
print(amro.display_user_balance())
print(suad.display_user_balance())
amro.transfer_money(suad,250)
print(amro.display_user_balance())
print(suad.display_user_balance())