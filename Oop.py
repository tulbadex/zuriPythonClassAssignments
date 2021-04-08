class Animal:
    animal_type = 'mammal'
    counter = 0

    def __init__(self, name, number_of_legs):
        # super(Aminal, self).__init__(*args)
        self.name = name
        self.number_of_legs = number_of_legs
        Animal.counter += 1
    
    def can_run(self):
        print(f"Animal {self.name} run with {self.number_of_legs} legs")


    # this ia available to the object when initiated automatical
    @classmethod
    def can_see(cls):
        print("All animal can see")

    @staticmethod
    def tail_wiggle():
        print("animal can wiggle is tail")



animal_one = Animal('hen', 2)
animal_two = Animal('dog', 4)
animal_three = Animal('cat', 4)

animal_one.can_run()
animal_two.can_run()
animal_three.can_run()

print("=" * 20)
print(animal_one.animal_type)
print(animal_two.animal_type)
print(animal_three.animal_type)

# print(Animal.counter)

print("=" * 40)

animal_one.can_see()
animal_two.can_see()
animal_three.can_see()

print(Animal.counter)
# print(animal_three.counter)