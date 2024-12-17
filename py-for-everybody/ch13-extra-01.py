# objects and classes

class Sample:

    def __init__(self):
        self.x = 0      # Publie
        self.__y__ = 0  # Private

    def inc_x(self):
        self.x += 1

    def print_x(self):
        print(f"x: {self.x}")

    def inc_y(self):
        self.__y__ += 1

    def print_y(self):
        print(f"y: {self.__y__}")

test = Sample()

test.print_x()
test.inc_x()
test.print_x()

test.print_y()
test.inc_y()
test.print_y()

# print(f"dir: {dir(test)}")
print(f"type: {type(test)}")
print(f"type: {type(test.x)}")
print(f"type: {type(test.inc_x)}")
print(f"type: {type(test.y)}")
print(f"type: {type(test.inc_y)}")

test.x += 1
test.print_x()

try:
    test.x += 1
    test.print_x()
except Exception as e:
    print(f"ERROR: {e}")

