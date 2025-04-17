# Questions for interview candidates:
# What does this code do?


def mystery_operation(input_str):
    length = len(input_str)
    output_str = ''

    for i in range(length-1, -1, -1):
        output_str += input_str[i]

    return output_str


print(mystery_operation('abcde'))


'''
Output

edcba
'''
