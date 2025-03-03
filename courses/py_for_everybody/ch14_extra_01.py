# objects and classes

class Sample:

    def __init__(self):
        self.x = 0    # Publie
        self.__y = 0  # Private

    def inc_x(self):
        self.x += 1

    def print_x(self):
        print(f"x: {self.x}")

    def inc_y(self):
        self.__y += 1

    def print_y(self):
        print(f"y: {self.__y}")

test = Sample()

test.print_x()
test.inc_x()
test.print_x()
test.x += 1
test.print_x()

# print(f"dir: {dir(test)}")
print(f"type: {type(test)}")
print(f"type: {type(test.x)}")
print(f"type: {type(test.inc_x)}")

print()

test.print_y()
test.inc_y()
test.print_y()

try:
    test.__y += 1
    test.print_y()
except Exception as e:
    print(f"ERROR: {e}")

try:
    print(f"type: {type(test.__y)}")
    print(f"type: {type(test.inc_y)}")
except Exception as e:
    print(f"ERROR: {e}")

