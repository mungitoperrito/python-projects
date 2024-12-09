# Count the number of times a word appears in a file
import string
import sys

def get_args():
    if len(sys.argv) != 2:
        print('Needs a filename')
        exit()

    return sys.argv[1]

def get_file_handle(filename):
    try:
        fh = open(filename, encoding="utf8")
    except Exception as e:
        print(f"Can't open file: {filename}")
        print(e)
        exit()

    return fh

def get_words(file_handle):
    words = dict()
    this_line = []


    for line in fh:
        line = line.lower()
        line = line.translate(line.maketrans('', '', string.punctuation))
        this_line = line.split()
        for word in this_line:
            words[word] = words.get(word, 0) + 1

    return words

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
words = get_words(fh)

sorted_words = sort_by_count(words) 
print(f"First {DISPLAY_COUNT} of {len(words)}")
for dc in range(DISPLAY_COUNT):
    print(f"{list(sorted_words.items())[dc]}")

