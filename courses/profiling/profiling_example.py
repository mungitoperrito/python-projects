# Demonstration module from blog site

import time
import random

def process_data(data):
    result = []
    for item in data:
        result.append(process_item(item))
    return result

def process_item(item):
    # Simulate processing time
    time.sleep(0.0001)  # Small delay for demonstration purposes
    return item * 2

def generate_data(size):
    return [random.randint(1, 100) for _ in range(size)]

def process_data_optimized(data):
    return [process_item(item) for item in data]

def main():
    data = generate_data(50)
    result1 = process_data(data)
    result2 = process_data_optimized(data)
    assert result1 == result2
    return result1

if __name__ == "__main__":
    main()
