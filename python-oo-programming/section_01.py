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
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Method def
    def bark(self):
        print("Woof woof")

# Create some dog objects
dog_01 = Dog("Bowser", "Terrier")
dog_02 = Dog("Firulais", "Mutt")

# # Uncomment to test methods
# dog_01.bark()
# dog_02.bark()

# View attributes
for dog in [dog_01, dog_02]:
    print(f"{dog.name} is a {dog.breed}")