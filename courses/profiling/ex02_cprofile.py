import cProfile
import pstats

# Sample functions to profile
def sum_current_inputs(num01, num02, num03):
    return num01 + num02 + num03


def count_some_stuff():
    sum = 0                           # Assignment
    count = 0

    for i in range(100):               # Loop
        for j in range(200):
            for k in range(250):
                if i == j :           # Conditional
                    continue
                elif j == k:
                    continue
                else:
                    sum += sum_current_inputs(i, j, k)
                    count += 1

    print(f'Count: {count}  Sum: {sum}')          # Function call

# Profile the function
profiler = cProfile.Profile()      # Set up the profiler
profiler.enable()
count_some_stuff()                 # Run the function
profiler.disable()

# View profile results
stats = pstats.Stats(profiler)

# Sort by some metrics
stats.sort_stats('cumulative').print_stats(10)  # Top 10 functions by cumulative time
stats.strip_dirs().sort_stats('calls').print_stats(10)  # Top 10 functions by call count
stats.strip_dirs().sort_stats('time').print_stats(10)  # Top 10 functions by time
stats.strip_dirs().sort_stats('time').print_stats(10)  # Top 10 functions by time



''' Sample output
Count: 4955100  Sum: 1356957350
         4955103 function calls in 1.468 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.036    1.036    1.468    1.468 /mnt/e/FILES/projects/python-projects/courses/profiling/ex02_cprofile.py:9(count_some_stuff)
  4955100    0.431    0.000    0.431    0.000 /mnt/e/FILES/projects/python-projects/courses/profiling/ex02_cprofile.py:5(sum_current_inputs)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4955103 function calls in 1.468 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  4955100    0.431    0.000    0.431    0.000 ex02_cprofile.py:5(sum_current_inputs)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    1.036    1.036    1.468    1.468 ex02_cprofile.py:9(count_some_stuff)


         4955103 function calls in 1.468 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.036    1.036    1.468    1.468 ex02_cprofile.py:9(count_some_stuff)
  4955100    0.431    0.000    0.431    0.000 ex02_cprofile.py:5(sum_current_inputs)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4955103 function calls in 1.468 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.036    1.036    1.468    1.468 ex02_cprofile.py:9(count_some_stuff)
  4955100    0.431    0.000    0.431    0.000 ex02_cprofile.py:5(sum_current_inputs)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

