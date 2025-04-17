# Questions for interview candidates:
# What does this code do?


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


input_list = ['a', 'b', 'c', 'd', 'e']

print(f"Mystery function 01: {mystery_function_01(input_list)}")
print(f"Mystery function 02: {mystery_function_02(input_list)}")


'''
Both functions print out pairs of values.
mystery_function_01: prints (a,b) and (b,a)
mystery_function_02: only prints (a,b)

Mystery function 01:
[('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'),
   ('b', 'a'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('b', 'e'),
     ('c', 'a'), ('c', 'b'), ('c', 'c'), ('c', 'd'), ('c', 'e'),
       ('d', 'a'), ('d', 'b'), ('d', 'c'), ('d', 'd'), ('d', 'e'),
         ('e', 'a'), ('e', 'b'), ('e', 'c'), ('e', 'd'), ('e', 'e')]

Mystery function 02:
[('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'),
             ('b', 'b'), ('b', 'c'), ('b', 'd'), ('b', 'e'),
                         ('c', 'c'), ('c', 'd'), ('c', 'e'),
                                     ('d', 'd'), ('d', 'e'),
                                                 ('e', 'e')]
'''