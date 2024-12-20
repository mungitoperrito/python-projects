# https://www.py4e.com/html3/03-conditional
# Exercise 1

BASE = 40               # Number of regular hours
OVERTIME_RATE = 1.5     # Multiplier for more than BASE hours

hours = float(input('How many hours: '))
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