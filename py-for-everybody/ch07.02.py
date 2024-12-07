# https://www.py4e.com/html3/07-files
# Exercise 2

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

def find_numbers(file_handle):
    found_numbers = []

    for line in fh:
        if line.startswith('X-DSPAM-Confidence'):
            num_string = line.rstrip().split(':')[1]
            found_numbers.append(float(num_string))

    return found_numbers        

############
### MAIN ###
############
filename = get_args()
fh = get_file_handle(filename)
numbers = find_numbers(fh)
print(numbers)