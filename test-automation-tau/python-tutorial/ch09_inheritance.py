# https://testautomationu.applitools.com/python-tutorial/chapter9.html
# Classes - inheritance

# Example 01
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_src(self):
        print("Base class")


############
### MAIN ###
############

if __name__ == "__main__":
    steve = Person("steve", "mitsis")
    steve.print_src()