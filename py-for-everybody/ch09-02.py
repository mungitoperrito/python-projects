# https://www.py4e.com/html3/09-dictionaries
# Exercise 2

import sys

def get_args():
    if len(sys.argv) != 2:
        print('Needs a filename')
        exit()

    return sys.argv[1]

def get_file_handle(filename):
    try:
        fh = open(filename)
    except Exception as e:
        print(f"Can't open file: {filename}")
        print(e)
        exit()

    return fh

def get_day_counts(file_handle):
    days = dict()
    this_line = []

    for line in fh:
        if line.startswith("From "):
            this_line = line.split()
            day = this_line[2].lower()
            days[day] = days.get(day, 0) + 1

    return days

############
### MAIN ###
############
filename = get_args()
fh = get_file_handle(filename)
day_counts = get_day_counts(fh)

# Print results in order
week = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
for d in week:
    print(f"{d}: {day_counts[d]}", end='')
    if d != 'sat':
        print(' ', end='')
print()
