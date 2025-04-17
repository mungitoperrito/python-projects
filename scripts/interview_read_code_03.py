# Questions for interview candidates:
# What does this code do?

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


'''
OUTPUT

Option one
Option four
a

'''