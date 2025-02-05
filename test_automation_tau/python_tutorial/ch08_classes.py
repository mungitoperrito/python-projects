# https://testautomationu.applitools.com/python-tutorial/chapter8.html
# Classes - scratch


# Example 01
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_person(self):
        print(f"fname: {self.fname}, lname: {self.lname}")

############
### MAIN ###
############
if __name__ == "__main__":
    bobby = Person("bob", "ramos")
    print(bobby)
    bobby.print_person()

    # Fails - needs two arguments
    # no_lname = Person("fname")
    # print(no_lname)