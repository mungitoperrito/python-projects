# https://www.py4e.com/html3/09-dictionaries
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

def get_words(file_handle):
    words = dict()
    this_line = []

    for line in fh:
        this_line = line.split().lower()
        for word in this_line:
            words[word] += words.get(word, 0) + 1
    
    return words

############
### MAIN ###
############
filename = get_args()
fh = get_file_handle(filename)
words_in_file = get_words(fh)
print(list(words.keys).sort())