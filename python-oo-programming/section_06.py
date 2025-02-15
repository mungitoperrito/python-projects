# Static attributes

# # Example 01
# class User:
#     # Class attributes
#     user_count = 0

#     #Instance attributes
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#         # Track number of instances
#         User.user_count += 1



# ############
# ### MAIN ###
# ############
# if __name__ == "__main__":
#     user_01 = ['Wild Bill', 'wildbill@pecos.edu']

# print(user_01)


########### NEW EXAMPLE

class Account:
    MIN_BALANCE = 100

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    # Instance method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${str(amount)}.", end='')
            print(f" Balance for {self.owner} is: {str(self._balance)}")

    @staticmethod
    def is_valid_interest_rate(rate):
        # Return True if rate is between 0 and 5
        return 0 <= rate <=5

account_01 = Account("Dave", 50.00)
account_01.deposit(5.0)

print(Account.is_valid_interest_rate(3))
print(Account.is_valid_interest_rate(10))