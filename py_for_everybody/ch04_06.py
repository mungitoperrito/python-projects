# https://www.py4e.com/html3/04-functions
# Exercise 6

BASE = 40               # Number of regular hours
OVERTIME_RATE = 1.5     # Multiplier for more than BASE hours

def get_hours():
    hours = -1.0
    try: 
        hours = float(input('How many hours: '))
    except:
        print('Hours must be an int or float.')
        print('Hours must be non-negative.')
        hours = float(input('How many hours: '))

    return hours

def get_rate():
    rate = -1.0
    try:     
        rate = float(input('Rate: '))
    except:
        print('Rate must be an int or float.')
        print('Rate must be non-negative.')
        rate = float(input('Rate: '))
  
    return rate

def get_values():
    hours = -1.0
    while hours < 0:
        hours = get_hours()

    rate = -1.0
    while rate < 0:
        rate = get_rate()

    return hours, rate       

def compute_pay(hours, rate):
    overtime_hours = 0

    if hours > BASE:
        base_hours = BASE
        overtime_hours = hours - BASE
    else:
        base_hours = hours

    base_pay = base_hours * rate
    overtime_pay = overtime_hours * rate * OVERTIME_RATE    

    return round(base_pay + overtime_pay, 2)

############
### MAIN ###
############

hours, rate = get_values()
total_pay = compute_pay(hours, rate)

print(f"Pay is {total_pay}")