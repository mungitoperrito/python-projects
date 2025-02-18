##############

# # Everything is an object. Objects come from classes
# name = "Dave"
# age = 18

# print(type(name.lower()))
# print(type(age))

# print(name)
# print(name.upper())

##############
# Simple classes

# Class def
class Dog:
    # Attributes
    def __init__(self, name, breed, owner=''):
        self.name = name
        self.breed = breed
        self.owner = owner

    # Method def
    def bark(self):
        print("Woof woof")

class Owner:
    def __init__(self, name, address='', number=''):
        self.name = name
        self.address = address
        self.phone_number = number


# Creat some owners
owner_01 = Owner("Dave")
owner_02 = Owner("Janet")

# Create some dog objects
dog_01 = Dog("Bowser", "Terrier", owner_02)
dog_02 = Dog("Firulais", "Mutt", owner_01)

# # Uncomment to test methods
# for dog in [dog_01, dog_02]:
#   dog.bark()

# View attributes
for dog in [dog_01, dog_02]:
    print(f"{dog.name} is a {dog.breed}, owner is: {dog.owner.name}")