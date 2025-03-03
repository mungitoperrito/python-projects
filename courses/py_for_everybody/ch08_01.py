# py-for-everybody/ch07.02.py
# Exercise 1

def chop(lst):

    if len(lst) < 3:
        print('List is too short')
        exit()

    del lst[0]
    del lst[-1]

    return None

def middle(lst):

    if len(lst) < 3:
        print('List is too short')
        exit()

    new_list = lst[1:-1] 
    return new_list

############
### MAIN ###
############
list_01 = ['a', 'c', 'f']
list_02 = ['a', 'c', 'f']

print(f"Start: {list_01 == list_02}")

chop(list_01)
list_02 = middle(list_02)

print(f"End: {list_01 == list_02}")
print(f"list_01: {list_01}")
print(f"list_02: {list_02}")