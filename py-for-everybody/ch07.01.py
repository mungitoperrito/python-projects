# https://www.py4e.com/html3/07-files
# Exercise 1

import sys
FILENAME = sys.argv[1]

def get_file_handle(filename):
    try:
        fh = open(FILENAME)
    except Exception as e:
        print(f"Can't open file: {FILENAME}")
        print(e)
        exit()

    return fh

############
### MAIN ###
############
fh = get_file_handle(FILENAME)