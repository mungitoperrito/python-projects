# https://testautomationu.applitools.com/python-tutorial/chapter4.html
# Conditionals - scratch

# # Example 01
# def if_then_else(input_str):
#     if input_str == "match01":
#         print(f"if: {input_str}")

#     elif input_str == "match02":
#         print(f"elif: {input_str}")

#     else:
#         print(f"else: {input_str}")


# Example 02
def add(num01, num02):
    print(f"{num01} + {num02} = {num01 + num02}")


def subtract(num01, num02):
    print(f"{num01} - {num02} = {num01 - num02}")


def multiply(num01, num02):
    print(f"{num01} * {num02} = {num01 * num02}")


def divide(num01, num02):
    print(f"{num01} / {num02} = {num01 / num02}")

def run_operation(operation, numbers):
    if operation == '+':
        add(numbers[0], numbers[1])
    
    elif operation == '-':
        subtract(numbers[0], numbers[1])
  
    elif operation == '*':
        multiply(numbers[0], numbers[1])
  
    elif operation == '/':
        divide(numbers[0], numbers[1])
  
    else:
        print(f"Error: {operation} not found.")

############
### MAIN ###
############

if __name__ == "__main__":

    # # Example 01
    # input_strings = ["match01", "match02", "match03"]

    # for s in input_strings:
    #     if_then_else(s)

    # Example 02
    operations = ['+', '-', '*', '/', '$']
    nums = [(0,1), (10,5)]

    for o in operations:
        for n in nums:
            run_operation(o, n)