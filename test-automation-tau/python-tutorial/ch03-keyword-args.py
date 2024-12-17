# https://testautomationu.applitools.com/python-tutorial/chapter3.html
# Keyword args - scratch

# # Example01
# def user_info(name, age, city):
#     print("{} is {} years old, from {}".format(name, age, city))

# user_info("Name01", 42, "City01")

# # Example02
# # Sets default positional args
# def user_info(name, age=0, city="City01"):
#     print("{} is {} years old, from {}".format(name, age, city))

# user_info("Name01")
# user_info("Name02", 20)
# user_info("Name03", 35, "City03")
# user_info(city="City04", name="Name04", age=42)

# Example 03
# *args
def addition(*args):
    print(sum(args))

addition()            # NOTE: Converts no arg to 0
addition(1,2)
addition(1,2,3)