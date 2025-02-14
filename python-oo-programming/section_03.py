class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def greet_user(self, user):
        print(f"Hi {user.username} from {self.username}")

user_01 = User("Dan", "dan@abc.com", "abc123")
user_02 = User("Bob", "bob@abc.com", "123abc")

user_01.greet_user(user_02)