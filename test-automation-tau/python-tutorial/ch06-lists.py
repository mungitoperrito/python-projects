# https://testautomationu.applitools.com/python-tutorial/chapter6.html
# Lists - scratch

# Example01
import string

list_01 = ["a", "b", "v", "a", "b"]

list_02 = list_01[:]

print(string.ascii_lowercase[0:5])           # Works
# list_03 = list_01[:].extend(string.ascii_lowercase[0:5]) # Doesn't work
list_03 = list_01[:]                         # Works
for c in string.ascii_lowercase[0:5]:
    list_03.append(c)

print(list_01)
print(list_02)
print(list_03)