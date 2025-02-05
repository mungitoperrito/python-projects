# Random

import random

rand_list = []

for i in range(10):
    rand_list.append(random.random())

print(rand_list)

for i in range(3):
    print(random.choice(rand_list))

