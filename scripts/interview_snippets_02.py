########################################################################
# QUESTION: Check if a string is a palindrome                          #
########################################################################

# def is_palindrome(str_to_check):
#     reversed = str_to_check[::-1]
#     return reversed == str_to_check

# for s in ['abc', 'fghjhgf', '', 'aab']:
#     print(f"string: {s} palindrome? {is_palindrome(s)}")

#     # Needs a check for empty string edge case


########################################################################
# QUESTION: Find the factorial of a positive integer                   #
########################################################################

# def factorial_01(n):
#     factorial = 1
#     while n > 0:
#         factorial *= n
#         n -= 1

#     return factorial

# # Recursive function
# def factorial_02(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_02(n-1)

# # Check the function
# for n in [0, 3, 10]:
#     # 0! == 1 by definition
#     # Correct values: 1, 6, 3628800
#     print(f"n: {n}  factorial: {factorial_02(n)}")

########################################################################
# QUESTION: Demonstrate bubble sort                                    #
########################################################################

# import random

# def bubble(unsorted_list):
#     num_elements = len(unsorted_list)
#     for i in range(num_elements - 0):
#         print(unsorted_list)
#         for j in range(num_elements - i - 1):
#             if unsorted_list[j] > unsorted_list[j + 1]:
#                 unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

# # Create some sample data
# unsorted = [random.randint(0,100) for _ in range(10) ]

# # Sort the data
# bubble(unsorted)

