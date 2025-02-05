# https://www.py4e.com/html3/08-lists
# Exercise 4

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
    this_line = list()

    for line in file_handle.readlines():
        this_line = line.lower().split()
        for word in this_line:
            words[word] = words.get(word, 0) + 1

    return words

def parse_words(word_dict):
    unique_words = list(word_dict.keys())
    unique_words.sort()

    return unique_words

############
### MAIN ###
############

file_name = get_args()
file_handle = get_file_handle(file_name)
word_dict = get_words(file_handle)
unique_words = parse_words(word_dict)

print(unique_words)
print(len(unique_words))