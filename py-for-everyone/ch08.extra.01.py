# mutability

var_str1 = 'abc'
var_str2 = 'abc'                  # Points to the same place as 1
var_int1 = 123
var_int2 = 123                    # Points to the same place as 1
var_list1 = ['a', 'b', 'c']
var_list2 = ['a', 'b', 'c']       # Points to a different place than 1
var_list3 = var_list2             # Alt name for var_list2
var_list4 = var_list2[:]          # Copies var_list2
var_list3.append('d')             # Also updates var_list2

strs1 = [var_str1, var_str2]
ints1 = [var_int1, var_int2]
lsts1 = [var_list1, var_list2, var_list3, var_list4]

print('strings original')
for s in strs1:
    print(f"{id(s)}:   {s}")
print('')

print('integers original')
for i in ints1:
    print(f"{id(i)}:   {i}")
print('')

print('lists original')
for l in lsts1:
    print(f"{id(l)}:   {l}")
print('')

print('')

# Update
var_str1 = 'abcd'                  # Creates new variable w/ same name
var_str2 = 'abcd'                 
var_int1 = 1234                    # Creates new variable w/ same name
var_int2 = 1234                    
var_list1 = ['a', 'b', 'c', 'd']   # Creates new variable w/ same name
var_list2 = ['a', 'b', 'c', 'd']   # Creates new variable w/ same name
var_list3 = var_list2
var_list4 = var_list2[:]
var_list3.append('e')              # Also updates var_list2

strs2 = [var_str1, var_str2]
ints2 = [var_int1, var_int2]
lsts2 = [var_list1, var_list2, var_list3, var_list4]

print('strings updated')
for s in strs2:
    print(f"{id(s)}:  {s}")
print('')

print('integers updated')
for i in ints2:
    print(f"{id(i)}:   {i}")
print('')

print('lists updated')
for l in lsts2:
    print(f"{id(l)}:   {l}")
print('')

print('')