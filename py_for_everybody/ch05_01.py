# https://www.py4e.com/html3/05-iterations
# Exercise 1

def get_input():
    int_vals = []

    val = None
    while True:
        try:
            val = input('Input an integer: ')
            if val.lower() == 'done':
                return int_vals
            else:
                try:
                    val = int(val)
                    int_vals.append(val)
                except:
                    print("Neither done nor int")             
        except:
            print('Enter an integer or "Done" to end input.')      

def print_stats(lst):
    print(f"list: {lst}")
    print(f"Total: {sum(lst)} count: {len(lst)}", end='')
    print(f" ave: {sum(lst)/len(lst)}, min: {min(lst)}  max: {max(lst)}")


############
### MAIN ###
############

int_vals = get_input()
if len(int_vals) > 0:
    print_stats(int_vals)
else:
    "No values to work with"

