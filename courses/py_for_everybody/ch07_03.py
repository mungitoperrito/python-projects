# https://www.py4e.com/html3/07-files
# Exercise 3

import sys

def get_args():
    if len(sys.argv) != 2:
        print('Needs a filename')
        exit()

    return sys.argv[1]

def get_file_handle(filename):
    if filename == 'easter egg':
        print('BOOM')
        exit()
    try:
        fh = open(filename)
    except Exception as e:
        print(f"Can't open file: {filename}")
        print(e)
        exit()

    return fh


############
### MAIN ###
############
filename = get_args()
fh = get_file_handle(filename)
print(fh)