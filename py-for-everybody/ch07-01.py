# https://www.py4e.com/html3/07-files
# Exercise 1

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

def print_lines(file_handle):
    for line in fh:
        print(line.rstrip().upper())

############
### MAIN ###
############
filename = get_args()
fh = get_file_handle(filename)
print_lines(fh)