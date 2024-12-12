# https://www.py4e.com/html3/06-strings
# Exercise 5

# Find
str = 'X-DSPAM-Confidence: 0.8475'

pos_colon = str.find(':')
number = float(str[pos_colon + 2:]) 
print(f"number: {number} type: {type(number)}") 