class Budget:

    def __init__(self, category):
        self.category = category
        self.amount = 1000

    def deposit(self, amount):
        self.amount += amount
        return self.amount

    def check_balance(self, amount):
        if self.amount < amount:
            return False
        else:
            return True

    def withdraw(self, amount):
        self.amount -= amount
        return self.amount

    def transfer(self, amount, category):
        if self.check_balance(amount) == True:
            self.amount -= amount
            category.amount += amount
            return "You have trasnfered {} to {}".format(amount, category.category )
        else:
            return "You do not have enoght balance to perfom this transaction"
            


clothing = Budget("Clothing")
# print(f"{clothing.deposit(5000)} has been deposited for clothing" )
print("{} has been deposited for clothing" .format(clothing.deposit(5000)) )
print(clothing.withdraw(2000))

food = Budget("Food")
transfer = clothing.transfer(1000, food)
print(transfer)
print(food.amount)
print(clothing.amount)

entertainment = Budget("Entertainment")