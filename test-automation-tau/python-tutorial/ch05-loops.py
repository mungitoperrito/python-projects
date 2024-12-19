# https://testautomationu.applitools.com/python-tutorial/chapter5.html
# Loops - scratch

# # Example 01
# fruits = ["apple", "orange", "pears", "cherries", "grapes"]

# for fruit in fruits:
#     print(f"This fruit: {fruit}")

# # Example 02
# fruits = ["apple", "orange", "pears", "cherries", "grapes"]

# for i in range(1,len(fruits), 2): # gets odd indexed items
# # for i in range(0,len(fruits), 2): # gets even indexed items
#     print(f"This fruit: {fruits[i]}")

# # Example 03
# for i in range(10):
#     if i % 2 == 0:
#         print("continue") # Skips even values
#     elif i == 5:
#         pass   # Effect is similar to continue in this case
#     else:
#         print(i)

#     print("end if-else block")

# Example 04
#   mean approaches RANGE_END, drops by .25 to .3 at high values
#   median approached expected
#   mode is random
import random
import statistics

NUM_TRIALS = 10000
RANGE_END = 200
RANGE_START = 1

def get_expected_number_of_runs(items, percent=0.5):
    chance_not_one_run = (1 - 1 / items)
    count = 1
    total_chance_not = 0
    while total_chance_not < percent:
        total_chance_not = 1 - chance_not_one_run ** count
        # print(round(total_chance_not,3))
        count += 1

    return count

    '''
    For each trial:
    pick a number, trial_end, between start and end
    pick a random number
    if it matches trial_end, return num_attempts
    if not, pick another random number and repeat
    '''
def run_trial(start, end, trial_end):
    num_attempts = 0

    while True:
            num_attempts += 1
            rn = random.randint(start, end) # inclusive range
            if rn == trial_end:
                break

    return num_attempts

############
### MAIN ###
############

count_num_runs = []
trial_end = random.randint(RANGE_START, RANGE_END)

for i in range(NUM_TRIALS):
     count_num_runs.append(run_trial(RANGE_START, RANGE_END, trial_end))

expected = get_expected_number_of_runs((RANGE_END - RANGE_START) + 1)
mean = statistics.mean(count_num_runs)
median = statistics.median(count_num_runs)
mode = statistics.mode(count_num_runs)

print(f"Range: {RANGE_START} to {RANGE_END}")
print(f"Repetitions: {NUM_TRIALS}")
print(f"Expected: {round(expected, 2)}")
print(f"Mean: {mean} Median: {median} Mode: {mode}")