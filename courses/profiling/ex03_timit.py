import timeit
from profiling_example import generate_data, process_data, process_data_optimized

DATA_SIZE = 1000           # Start small to verify functionality
NUM_REPS = 10              # Number of times to repeat the timing test

# Method 1: Basic string evaluation
# Have to redo imports and constant defs inside the setup_basic code
setup_basic = """
from profiling_example import generate_data, process_data
DATA_SIZE = 10
data = generate_data(DATA_SIZE)
"""
basic_time = timeit.timeit('process_data(data)', setup=setup_basic, number=NUM_REPS)
print(f"Basic timing: {basic_time:.4f} seconds")


# Method 2: Using lambda for better control
data = generate_data(DATA_SIZE)
advanced_time = timeit.timeit(lambda: process_data(data), number=NUM_REPS)
print(f"Advanced timing: {advanced_time:.4f} seconds")


# Method 3: Comparing implementations
data = generate_data(DATA_SIZE)
original_time = timeit.timeit(lambda: process_data(data), number=NUM_REPS)
optimized_time = timeit.timeit(lambda: process_data_optimized(data), number=NUM_REPS)
print(f"Original implementation: {original_time:.4f} seconds")
print(f"Optimized implementation: {optimized_time:.4f} seconds")
print(f"Improvement ratio: {original_time/optimized_time:.2f}x")

