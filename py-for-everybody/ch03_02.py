# https://www.py4e.com/html3/03-conditional
# Exercise 2

BASE = 40               # Number of regular hours
OVERTIME_RATE = 1.5     # Multiplier for more than BASE hours

try: 
    hours = float(input('How many hours: '))
except:
    print('Hours must be an int or float.')
    hours = float(input('How many hours: '))

try:     
    rate = float(input('Rate: '))
except:
    print('Rate must be an int or float.')
    rate = float(input('Rate: '))
  

overtime_hours = 0

if hours > BASE:
    base_hours = BASE
    overtime_hours = hours - BASE
else:
    base_hours = hours

base_pay = base_hours * rate
overtime_pay = overtime_hours * rate * OVERTIME_RATE    
total_pay = round(base_pay + overtime_pay, 2)

print(f"Pay is {total_pay}")