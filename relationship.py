# super class
class Animal:
    ''' def __init__(self, *args):
        super(Animal, self).__init__(*args)) '''
    
    def can_breath(self):
        return "This animal can breath"

# inheretance and make seperation of concern effective
# sub class
class Mammals(Animal):
    ''' def __init__(self, *args):
        super(Mammals, self).__init__(*args)) '''

    def body_size(self):
        return "Body size need to be 40kg and above"
        
mammal_one = Mammals()
print(mammal_one.can_breath())
print(mammal_one.body_size())



# Inherentance -----> shows is a relationship
# Composition -------> shows has a relationship