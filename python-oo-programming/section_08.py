# Encapsulation

class BankAccount:
    def __init__(self):
        self._balance = 0.0


    @property
    def balance(self):
        return self._balance


    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount


    def withdrawal(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Withdrawal amount must be less than balance")
        self._balance -= amount


############
### MAIN ###
############

if __name__ == "__main__":
    account_01 = BankAccount()
    print(account_01.balance)

    # # Uncomment to test
    # account_01.deposit(-5)
    # print(account_01.balance)

    account_01.deposit(5)
    print(account_01.balance)

    # # Uncomment to test
    # account_01.withdrawal(500)
    # print(account_01.balance)

    # # Uncomment to test
    # account_01.withdrawal(-5)
    # print(account_01.balance)

    account_01.withdrawal(5)
    print(account_01.balance)

