import sys
import timeit as tm


#################
# Check version #
#################
# print(f'Python version: {sys.version}')

# OUTPUT
#  # Python version: 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0]


#############
# Basic use #
#############
# # Run the test number times: number = 1000
# exec_time = tm.timeit('"-".join(str(n) for n in range(1000))',
#                       number = 1000)
# print(f'Execution time: {exec_time}')

# # OUTPUT
# # Execution time: 0.1015612629998941


#############################################
# To isolate an operation, use a setup step #
#############################################

# setup_code = """
# data = [ i for i in range(1000)]
# """

# test_code_multiply = """
# result = [x * 2 for x in data]
# """

# test_code_subtract = """
# result = [x - 2 for x in data]
# """

# test_code_exponent = """
# result = [x ** 2 for x in data]
# """

# exec_time_subtract = tm.timeit(stmt=test_code_subtract, setup=setup_code, number=1000)
# print(f'Execution time sub: {exec_time_subtract}')

# exec_time_multiply = tm.timeit(stmt=test_code_multiply, setup=setup_code, number=1000)
# print(f'Execution time mlt: {exec_time_multiply}')

# exec_time_exponent = tm.timeit(stmt=test_code_exponent, setup=setup_code, number=1000)
# print(f'Execution time exp: {exec_time_exponent}')

# # OUTPUT
# '''
# Execution time sub: 0.026781700988067314
# Execution time mlt: 0.028598789998795837
# Execution time exp: 0.18564112999592908
# '''


#####################
# Compare functions #
#####################

data = list(range(1000))            # Define once, outside perf timing

def approach_01(data):
    return [ x * 2 for x in data]

def approach_02(data):
    return list(map(lambda x: x * 2, data))

exec_time_v01 = tm.timeit(lambda: approach_01(data), number = 1000)
print(f'Execution time v01: {exec_time_v01}')

exec_time_v02 = tm.timeit(lambda: approach_02(data), number = 1000)
print(f'Execution time v02: {exec_time_v02}')

print(f'Ratio v02/v01: {exec_time_v02/exec_time_v01:.2f}')

# OUTPUT
'''
Execution time v01: 0.027972252981271595
Execution time v02: 0.04827875300543383
Ratio v02/v01: 1.73
'''