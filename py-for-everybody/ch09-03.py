# https://www.py4e.com/html3/09-dictionaries
# Exercise 3

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
    addresses = dict()
    this_line = []

    for line in fh:
        if line.startswith("From "):
            this_line = line.split()
            address = this_line[1].lower()
            addresses[address] = addresses.get(address, 0) + 1

    return addresses

def sort_by_count(count_dict):
    # Doesn't work with python pre-3.6
    sorted_dict = dict()

    # # Uncomment for smallest to largest
    # sorted_dict = dict(sorted(
    #         count_dict.items(),
    #         key=lambda item: item[1]
    #         )
    #     )

    # Uncomment for largest to smallest
    sorted_dict = dict(sorted(
            count_dict.items(),
            key=lambda item: item[1],
            reverse=True
            )
        )

    return sorted_dict

############
### MAIN ###
############
DISPLAY_COUNT = 3

filename = get_args()
fh = get_file_handle(filename)
addresses = get_addresses(fh)

# # Uncomment to check list
# print(f"First 3: {list(addresses.keys())[:3]} of {len(addresses)}")

# Uncomment to print first sorted values
sorted_addresses = sort_by_count(addresses) 
print(f"First {DISPLAY_COUNT} of {len(sorted_addresses)}")
for dc in range(DISPLAY_COUNT):
    print(f"{list(sorted_addresses.items())[dc]}")

