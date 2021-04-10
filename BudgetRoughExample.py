class Budget:
    def __init__(self, name = ''):
        self.amount = 0
        self.name = name

    def check_fund(self, amount):
        if amount < 1:
            return False
        else:
            return True

    def deposit(self, amount):
        if self.check_fund(amount):
            depositFund =  self.amount + amount
            self.amount = depositFund
            # return depositFund
            return amount
        else:
            return 0

    def withdraw(self, amount):
        if self.check_fund(amount):
            withdrawFund = self.amount - amount
            self.amount = withdrawFund
            # return with
            # drawFund
            return amount
        else:
            return 0

    def get_balance(self):
        return self.amount

    def transferFund(self, amount, fromAcct):
        if self.check_fund(amount):
            fromAcct.amount -= amount 
            self.amount += amount 

            # return self.amount
            return amount
        else:
            return 0


''' food = Budget(int(7000), 'food')
clothing = Budget(int(5000), 'clothing')
entertainment = Budget(int(8000), 'entertainment') '''

food = Budget('food')
clothing = Budget('clothing')
entertainment = Budget('entertainment')

clothing.amount = 1000
food.amount = 10000
entertainment.amount = 20000

print(clothing.get_balance())
print(food.get_balance())
print(entertainment.get_balance())
print(entertainment.deposit(food.withdraw(-1)))
print(clothing.transferFund(500, food))
print(food.get_balance())
print(clothing.get_balance())
print(entertainment.get_balance())
print(food.transferFund(5000, entertainment))
print(food.get_balance())
print(clothing.get_balance())
print(entertainment.get_balance())

''' print(clothing.amount)
print(food.amount)
print(clothing.get_balance())
print(food.get_balance())
print(food.deposit(int(7000)))
print(clothing.amount)
print(food.amount)
print(clothing.get_balance())
print(food.get_balance())
print(food.withdraw(500))
print(clothing.get_balance())
print(food.get_balance())
print(clothing.transferFund(500, food, clothing))
print(clothing.get_balance())
print(food.get_balance()) '''

''' print(clothing.deposit(food.withdraw(500)))
print(clothing.get_balance())
print(food.get_balance()) '''

''' print(food.name)
print(food.amount)
# print(food.withdraw(2000))
print(food.deposit(2000))
print(food.amount)
print(food.withdraw(2000))
print(food.amount)
print(food.withdraw(5000))
print(food.amount) '''
        
''' clothing = Budget(int(7000), 'clothing')
print(clothing.name)
# print(clothing.cash + food.cash)
print(clothing.transferFund(2000, food.name)) '''