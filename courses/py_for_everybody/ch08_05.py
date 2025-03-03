# https://www.py4e.com/html3/08-lists
# Exercise 5

import sys

def get_args():
    if len(sys.argv) != 2:
        print('Needs a filename')
        exit()

    return sys.argv[1]

def get_file_handle(filename):
    try:
        fh = open(filename)
    except Exception as e:
        print(f"Can't open file: {filename}")
        print(e)
        exit()

    return fh

def get_addresses(file_handle):
    addresses = list()

    for line in file_handle.readlines():
        if line.startswith('From '):
            address = line.lower().split()[1]
            addresses.append(address)

    return addresses

############
### MAIN ###
############

file_name = get_args()
file_handle = get_file_handle(file_name)
addresses = get_addresses(file_handle)

for address in addresses:
    print(address)
print(f"There are {len(addresses)}.")