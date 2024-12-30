# https://testautomationu.applitools.com/python-tutorial/chapter9.html
# Classes - inheritance

# # Example 01
# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         self.annoyed = False


#     def print_src(self):
#         print("Base")

#     def print_annoyance(self):
#         print(f"Annoyed: {self.annoyed}")


# class Enemy(Person):
#     def __init__(self, fname, lname, enemies):
#         super().__init__(fname, lname)
#         self.enemies = enemies

#     def insult(self, other):
#         if other in self.enemies:
#             print(f"{self.fname} says, 'You suck {other}'")

#             # Can't use string to call class. Use globals dict instead
#             # Ch09 example calls a class, not a string
#             globals()[other].annoyed = True


############
### MAIN ###
############

if __name__ == "__main__":
    # Test base class
    # steve = Person("steve", "mitsis")
    # steve.print_src()

    # # Example 01
    # # Simple inheritance
    # steve = Person("steve", "mitsis")
    # frank = Enemy("frank", "jones", ["bob", "ted"])
    # paul = Enemy("paul", "smith", ["bob", "ted", "steve"])

    # frank.insult("steve")
    # steve.print_annoyance()
    # paul.insult("steve")
    # steve.print_annoyance()
