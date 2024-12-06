# list functions

import random

def create_list():
    var_list = []
    for i in range(10):
        val = random.randint(0,9)
        if val > 0:
            var_list.append(val)

    return var_list        

def print_list(lst):
    print(lst)
    print(f"Len: {len(lst)} Min: {min(lst)}",  end='')
    print(f" Max: {max(lst)} Sum: {sum(lst)}",  end='')
    print(f" Avg: {round(sum(lst)/len(lst), 2)}")
    print('')

for i in range(3):
    l = create_list()
    print_list(l)