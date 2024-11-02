def fib_recursive(n):
    if n == 0:
        return 0
       
    if n == 1:
        return 1

    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_recursive_cache(n):
    if not n in cache:
        cache[n] = fib_recursive_cache(n-1) + fib_recursive_cache(n-2)
    return cache[n]

def fib_iterative(n):
    old, new = 0, 1
    
    if n == 0:
        return 1
    
    for i in range(n-1): 
        old, new  = new, old + new

    return new

##########
## MAIN ##
##########

if __name__ == "__main__":
    import timeit

    # print(f"RECURSIVE: {fib_recursive(6)}")
    # print(f"ITERATIVE: {fib_iterative(6)}")

    test_values = [2, 5, 10, 50 ]

    print("Recursive")
    for i in test_values:
        start =  timeit.time.perf_counter_ns()
        fib_recursive(i)
        print(f"i: {i}  {timeit.time.perf_counter_ns() - start}")
    
    print("Iterative")
    for i in test_values:
        start =  timeit.time.perf_counter_ns()
        fib_iterative(i)
        print(f"i: {i}  {timeit.time.perf_counter_ns() - start}")

    print("Cache")
    cache = {0:0, 1:1}
    for i in test_values:
        start =  timeit.time.perf_counter_ns()
        fib_recursive_cache(i)
        print(f"i: {i}  {timeit.time.perf_counter_ns() - start}")