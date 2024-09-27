
def factorial(n):
    if(DEBUG): print(f"n: {n}")

    # No base case for 0 or negative numbers
    if n < 1:
        exit()

    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        if(DEBUG): print(f"n: {n} res: {res}")
        return res	

if __name__ == "__main__":
    DEBUG = True
    
    for i in range(1,5):
        print(f"RESULT: f: {i} {factorial(i)}")