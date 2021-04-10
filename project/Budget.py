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
            if self.amount > amount:
                withdrawFund = self.amount - amount
                self.amount = withdrawFund
                # return with
                # drawFund
                return amount
            else:
                return 0
        else:
            return 0

    def get_balance(self):
        return self.amount

    def transferFund(self, amount, fromAcct):
        if self.check_fund(amount):
            if self.amount > amount:
                fromAcct.amount -= amount 
                self.amount += amount 

                # return self.amount
                return amount
            else:
                return 0
        else:
            return 0



food = Budget('food')
clothing = Budget('clothing')
entertainment = Budget('entertainment')

# add budget to instance
clothing.amount = 1000
food.amount = 10000
entertainment.amount = 20000

print("="*10)
print("="*10 + " Get Balance of all categories" + "="*10)
print(clothing.get_balance())
print(food.get_balance())
print(entertainment.get_balance())

print("="*10)
print("="*10 + " Deposit Fund From Food to Entertainment" + "="*10)
print(entertainment.deposit(food.withdraw(500)))

print("="*10)
print("="*10 + " Transfer Fund From Food to Clothing" + "="*10)
print(clothing.transferFund(500, food))

print("="*10)
print("="*10 + " Get Balance of all categories" + "="*10)
print(food.get_balance())
print(clothing.get_balance())
print(entertainment.get_balance())

print("="*10)
print("="*10 + " Transfer Fund From Entertainment to Food" + "="*10)
print(food.transferFund(5000, entertainment))

print("="*10)
print("="*10 + " Get Balance of all categories" + "="*10)
print(food.get_balance())
print(clothing.get_balance())
print(entertainment.get_balance())
