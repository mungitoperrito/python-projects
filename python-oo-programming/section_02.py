class Person:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def greet(self):
        print(f"{self.name} is {self.age}")

# Uncomment to test
person_01 = Person("Dave", 100)
person_02 = Person("Bob", 50)

for p in [person_01, person_02]:
  p.greet()