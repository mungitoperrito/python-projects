input_list = ['a', 'b', 'c', 'd', 'e']

def mystery_function_01(input_list):
    output = []
    for outer_element in input_list:
        for inner_element in input_list:
            output.append((outer_element, inner_element))

    return output


def mystery_function_02(input_list):
    output = []
    for outer_element in range(len(input_list)):
        for inner_element in input_list[outer_element:]:
            output.append((input_list[outer_element], inner_element))

    return output


print(f"Mystery function 01: {mystery_function_01(input_list)}")
print(f"Mystery function 02: {mystery_function_02(input_list)}")


'''
Both functions print out pairs of values.
mystery_function_01: prints (a,b) and (b,a)
mystery_function_02: only prints (a,b)
'''