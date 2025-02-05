# Strings

# # Spaces and concatenation
# str_01 = 'aaa'
# print('Start' + str_01 + 'end')
# print('Start ' + str_01 + ' end')  # Needs spaces 

# # Case
# str_02 = 'AaA'
# print(str_02.lower())
# print(str_02.capitalize())

# # Count 
# str_03 = 'A long day at the office.'
# print(str_03.count('a'))  # counts occurances of string in string
# print(str_03.count('the'))
# print(str_03.count('not there'))

# Find
str_04 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

pos_at = str_04.find('@')            # searches from 0
print(pos_at)

pos_space = str_04.find(' ', pos_at) # searches from pos_at
print(pos_space)

host = str_04[pos_at + 1:pos_space]  # start after the @
print(host) 