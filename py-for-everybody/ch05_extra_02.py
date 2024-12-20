# min max
# Find extreme values in a list the hard way

import random

def create_list():
    lst = []
    for i in range(10):
        lst.append(random.randint(0,101))

    return(lst)

def find_max(lst):
    max_val = lst[0]
    for l in lst:
        if l > max_val:
            max_val = l
    
    return max_val

def find_min(lst):
    min_val = lst[0]
    for l in lst:
        if l < min_val:
            min_val = l
    
    return min_val

############
### MAIN ###
############
test_list = create_list()
print(f"list: {test_list}")
print(f"min: {find_min(test_list)}")
print(f"max: {find_max(test_list)}")