class User:
    def __init__(self, username, email, password):
        self.username = username
        # Protected, but only by convention
        self._email = email
        self.password = password

    def greet_user(self, user):
        print(f"Hi {user.username} from {self.username}")

user_01 = User("Dave", "aaa@corp.com", "abc")
user_02 = User("Bob", "bbb@corp.com", "abc")

for u in [user_01, user_02]:
  u.greet_user(user_01)