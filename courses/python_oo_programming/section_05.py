# Getters and setter from properties rather than methods

# Protected by convention, single underscore
class User:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        print("In property setup")
        return self._email

    @email.setter
    def email(self, value):
        # Sample of validation in setter
        if '@' in value:
            self._email = value

    @property
    def password(self):
        return self._password

user_01 = User("Dave", "aaa@corp.com", "abc")

print(user_01.email)
user_01.email = "Wont work"
print(user_01.email)
user_01.email = "bbb@firm.net"    # Works, meets validation
print(user_01.email)