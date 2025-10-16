########################################################################
# QUESTION: How many times does the letter 'a' appear in the first two #
#           paragraphs of Alice in Wonderland?                         #
########################################################################

paragraph_01 ="Alice was beginning to get very tired of sitting by her sister" \
              " on the bank, and of having nothing to do: once or twice she" \
              " had peeped into the book her sister was reading, but it had" \
              " no pictures or conversations in it, 'and what is the use of a" \
              " book,' thought Alice 'without pictures or conversations?'"

paragraph_02 ="So she was considering in her own mind (as well as she could," \
               " for the hot day made her feel very sleepy and stupid)," \
               " whether the pleasure of making a daisy-chain would be worth" \
               " the trouble of getting up and picking the daisies, when" \
               " suddenly a White Rabbit with pink eyes ran close by her."

# # Method 1
# # Uncomment to count just 'a'
# count_a = 0
# text = [paragraph_01, paragraph_02]
#
# # for paragraph in text:
#     for letter in paragraph.lower():
#         if letter == 'a':
#             count_a += 1

# print(f"count: {count_a}")

# # Method 2
# # Uncomment to count all letters
from collections import defaultdict
import string

counts = defaultdict(int)
text = [paragraph_01, paragraph_02]

for paragraph in text:
    for letter in paragraph.lower():
        # if letter in string.ascii_lowercase:     # Alternate approach
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            counts[letter] += 1

# # Uncomment to print all counts
# for (k,v) in sorted(counts.items()):
#     print(f"{k}: {v}")

# Uncomment to print just 'a' counts
print(f"count: {counts['a']}")




