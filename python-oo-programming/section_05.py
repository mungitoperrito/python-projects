# Getters and setters

# Protected by convention, single underscore
class User:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    @property
    def email(self):
        print("In property setup")
        return self._email

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

user_01 = User("Dave", "aaa@corp.com", "abc")
user_02 = User("Bob", "bbb@corp.com", "abc")

for u in [user_01, user_02]:
    print(u.email)