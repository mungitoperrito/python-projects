# Some short python interview problems.

# ### Print pairs of values
# input_list = ['a', 'b', 'c', 'd', 'e']

# # (a,b) and (b,a) both included
# pairs_01 = []
# for outer in input_list:
#     for inner in input_list:
#         pairs_01.append((outer, inner))

# print(f"Both included: {pairs_01}")

# # (a,b) or (b,a) included
# pairs_02 = []
# for outer in range(len(input_list)):
#     for inner in input_list[outer:]:
#         pairs_02.append((input_list[outer], inner))

# print(f"Unique: {pairs_02}")


# ### Reverse a string without using reverse
# def reverse_string(input_str):
#     length = len(input_str)
#     output_str = ''

#     for i in range(length-1, -1, -1):
#         output_str += input_str[i]

#     return output_str

# print(reverse_string('abcde'))


### What does this print?
def print_something(value):
    if value == 'a':
        print("Option one")
    elif value == 'b':
        exit()
        print("Option two")
    else:
        print("Option three")

    print("Option four")

    return(value)

for v in ['a', 'b', 'c']:
    returns = print_something(v)
    print(returns)

# Output:
# Option one
# Option four
# a

