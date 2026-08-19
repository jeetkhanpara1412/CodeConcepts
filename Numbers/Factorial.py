# The factorial of a positive integer n is the product of all positive integers from 1 to n.
# Factorial is not defined for negative integers.
# Formula => n!=n×(n−1)×(n−2)×...×2×1

# Examples
# 1! = 1
# 2! = 2 × 1 = 2
# 3! = 3 × 2 × 1 = 6

# Special Case

# 0! = 1


# 1: Using a for Loop (Most Common)

num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, num + 1):
        fact *= i

    print("Factorial =", fact)



# 2: Using a while Loop (Most Common)

# num = int(input("Enter a number: "))

# fact = 1
# i = 1

# while i <= num:
#     fact *= i
#     i += 1

# print("Factorial =", fact)



# 3: Using Recursion

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# num = int(input("Enter a number: "))
# print("Factorial =", factorial(num))



# 4: Using Built-in Function

# import math

# num = int(input("Enter a number: "))

# print("Factorial =", math.factorial(num))