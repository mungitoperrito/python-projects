# Protected, but only by convention
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def clean_email(self):
       return self._email.lower().strip()

user_01 = User("Dave", "aaa@corp.com", "abc")
user_02 = User("Bob", "  BBB@corp.com ", "abc")

for u in [user_01, user_02]:
  print(u._email)           # Breaks convention, but works
  print(u.clean_email())    # Expected way


