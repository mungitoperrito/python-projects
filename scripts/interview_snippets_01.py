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
# from collections import defaultdict
# import string

# counts = defaultdict(int)
# text = [paragraph_01, paragraph_02]

# for paragraph in text:
#     for letter in paragraph.lower():
#         # if letter in string.ascii_lowercase:     # Alternate approach
#         if letter in 'abcdefghijklmnopqrstuvwxyz':
#             counts[letter] += 1

# # Uncomment to print all counts
# # for (k,v) in sorted(counts.items()):
# #     print(f"{k}: {v}")

# # Uncomment to print just 'a' counts
# print(f"count: {counts['a']}")


########################################################################
# QUESTION: Write a function to reverse a string. Write some code to   #
#           test your function.                                        #
########################################################################

# def reverse_01(original_str):
#     # Explicit starting point
#     return original_str[len(original_str)::-1]

# def reverse_02(original_str):
#     # Implied starting point
#     return original_str[-1::-1]

# def reverse_03(original_str):
#     index = len(original_str)
#     return_value = ''

#     for i in range(index - 1, -1, -1):
#        return_value += original_str[i]

#     return return_value

# # Demonstrate function
# print(f"abcde: {reverse_03('abcde')}")

# # Test code
# input_string = 'abcde'

# # # Uncomment for failing test code
# # assert input_string == reverse_03(reverse_03(input_string)) + 'fail'

# # Passing test code
# assert input_string == reverse_03(reverse_03(input_string))


########################################################################
# QUESTION: Write a function that takes a positive integer and prints  #
#           the second odd number that is greater than the integer.    #
########################################################################


# def second_greater(start_int):
#     # Check if odd or even
#     if (start_int % 2 == 0):
#         return start_int + 3
#     else:
#         return start_int + 4

# if __name__ == '__main__':

#     for n in [1, 4, 5]:
#         print(f"number: {n}  2d odd number: {second_greater(n)}")

