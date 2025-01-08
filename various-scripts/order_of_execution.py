'''
Some print statements to show order of statement execution
'''


class Sample():
    print("CLASS DEF LINE 1")

    var1 = ''

    def __init__(self):
        print("\tCLASS INIT 1")
        self.var1 = 10

    def get_val(self):
        print("\tCLASS FUNC DEF LINE 1")
        return self.var1

    print("CLASS DEF END\n\n")


def main():
    print("IN FUNC LINE 1")
    s = Sample()
    print("\tIN FUNC AFTER CLASS INIT")
    print(f"\tRUN FUNCTION: {s.get_val()}")
    print("IN FUNC END\n\n")


if __name__ == "__main__":
    print("IF main LINE 1")
    main()
    print("IF main END")
