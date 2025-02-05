# https://www.py4e.com/html3/02-variables
# Exercise 5

temp_c = float(input('Temp in C: '))

print(f"Temp in F is {round( (9 / 5) * temp_c + 32, 2)}")

''' 
Test cases:

0     32
100   212
-40   -40
'''