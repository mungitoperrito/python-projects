# Protected methods

class Account:
    MIN_BALANCE = 100

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    # Instance method
    def deposit(self, amount):
        if self._is_valid_amount(10):
            self.__update_balance(amount)


    # Protected method (single underscore)
    def _is_valid_amount(self, amount):
        return amount > 0


    # Private method (double underscore)
    def __update_balance(self, amount):
        self.__balance += amount
        print(f"Deposited ${str(amount)}.", end='')
        print(f" Balance for {self.owner} is: {str(self.__balance)}")

# # Uncomment to test
# account_01 = Account("Dave", 50.00)
# account_01.deposit(5.0)


class NotSoSecret:
    def __init__(self):
        self.aaa = 'A'
        self._bbb = 'B'
        self.__ccc = 'C'

thing_01 = NotSoSecret()

print(thing_01.aaa)

print(thing_01._bbb)    # Works, poor practice

try:
    print(thing_01.__ccc)   # Fails, private
except:
    print("__ccc fails as expected")

try:
        print(thing_01._NotSoSecret__ccc)   # Should unmangle name
except:
    print("__ccc didn't unmangle")
