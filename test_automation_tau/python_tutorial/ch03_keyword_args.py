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

# # Example 03
# # *args
# def addition(*args):
#     print(sum(args))

# addition()            # NOTE: Converts no arg to 0
# addition(1,2)
# addition(1,2,3)

# # Example 04
# # **kwargs
# def user_info(**kwargs):
#     print(kwargs)

# user_info()            # NOTE: prints empty dict
# user_info(a="AA")
# user_info(a="AA", b="BBB", g=20)

# Example 05
# **kwargs, *args, pos
# def user_info(fname, lname="LN01", *args, **kwargs):
def user_info(fname, lname, *args, **kwargs):
    print("pos01: {} pos02: {} args: {}  kwargs: {}".format(
        fname, lname, args, kwargs
        )
    )

# user_info("FN01") # Too few args
user_info(lname="LN02", fname="FN02")  # Arg order changes
user_info("LN03", "FN03", 2, 4, 6)       # Postional args before keyword
user_info("LN04", "FN04", 2, 4, 6, "AA", "BB", "CC") # args eats all, no kword
user_info("LN04", "FN04", 2, 4, 6, "AA", b="BB", c="CC")

# # Example 06 (based on site ex)
# def application(fname, lname, email, company, *args, **kwargs):
#     print("{} {} works at {}. Her email is {}."\
#           .format(fname, lname, company, email))
#     print("{} {} works at {}. Her email is {}. args: {}, kwargs: {}"\
#           .format(fname, lname, company, email, args, kwargs))

# application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, \
#             hire_date = "September 2010")

# # Output keyword arg follows all the positional ones
# '''
# Jess Ingrass works at Teach Code. Her email is mail @ mail.com.
# Jess Ingrass works at Teach Code. Her email is mail @ mail.com. args: (75000,), kwargs: {'hire_date': 'September 2010'}
# '''