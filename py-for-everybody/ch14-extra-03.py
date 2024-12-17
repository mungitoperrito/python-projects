# objects - constructors

class Sample:

    shared_x = 0

    def __init__(self, name):
        self.x = 0
        self.name = name
        print(f"Created {self.name} val: {self.x}")

    def inc_x(self):
        self.x += 1
        print(f"x: {self.x}")
    
    def print_attributes(self):
        print(f"name: {self.name} x: {self.x} shared_x: {self.shared_x}")

print("\ns01")
s01 = Sample("s01")
s01.inc_x()
s01.print_attributes()

print("\ns02")
s02 = Sample("s02")
s02.print_attributes()

print("\nBoth")
s02.shared_x += 1           # Updates instance with local value
s01.print_attributes()
s02.print_attributes()

Sample.shared_x = 5           # Updates all instances, but doesn't
                              #  overwrite explicitly set local
s01.print_attributes()
s02.print_attributes()

print("\ns03")
s02 = Sample("s03")
s02.print_attributes()