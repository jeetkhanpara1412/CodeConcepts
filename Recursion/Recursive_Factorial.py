# The factorial of a number is the product of all positive integers from 1 to that number.

# Formula
# n!=n×(n−1)×(n−2)×...×1

# Examples
# 5! = 5 × 4 × 3 × 2 × 1 = 120

# 4! = 4 × 3 × 2 × 1 = 24

# 3! = 3 × 2 × 1 = 6

# 2! = 2 × 1 = 2

# 1! = 1

# 0! = 1


def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

# Test the function
num = 5
print(f"The factorial of {num} is {factorial(num)}")


# Iterative Version

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))