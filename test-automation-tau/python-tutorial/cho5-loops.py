# https://testautomationu.applitools.com/python-tutorial/chapter5.html
# Loops - scratch

# # Example 01
# fruits = ["apple", "orange", "pears", "cherries", "grapes"]

# for fruit in fruits:
#     print(f"This fruit: {fruit}")

# # Example 02
# fruits = ["apple", "orange", "pears", "cherries", "grapes"]

# for i in range(1,len(fruits), 2): # gets odd indexed items
# # for i in range(0,len(fruits), 2): # gets even indexed items
#     print(f"This fruit: {fruits[i]}")

# Example 03
for i in range(10):
    if i % 2 == 0:
        print("continue") # Skips even values
    elif i == 5:
        pass   # Effect is similar to continue in this case
    else:
        print(i)

    print("end if-else block")