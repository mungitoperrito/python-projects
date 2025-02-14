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

class Dog:
    def bark(self):
        print("Woof woof")

dog_01 = Dog()
dog_01.bark()