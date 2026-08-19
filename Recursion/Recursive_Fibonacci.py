# The Recursive Fibonacci algorithm calculates the Fibonacci sequence by calling the same function repeatedly.

# The Fibonacci sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Each number is the sum of the previous two numbers.

# Formula
# F(0) = 0
# F(1) = 1

# F(n) = F(n-1) + F(n-2)    for n > 1

def fibonacci(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = 6
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

