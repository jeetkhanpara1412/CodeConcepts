# 1. GCD (Greatest Common Divisor)
# The GCD of two numbers is the largest number that divides both numbers exactly

# Factors of 12 = 1, 2, 3, 4, 6, 12
# Factors of 18 = 1, 2, 3, 6, 9, 18

# Common Factors = 1, 2, 3, 6

# Greatest = 6

# GCD = 6


# Python Built-in Method

import math

num1 = 12
num2 = 18

print("GCD =", math.gcd(num1, num2))

import math

num1 = 12
num2 = 18

print("LCM =", math.lcm(num1, num2))

# *****************************************************

# 1 using loop 

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# gcd = 1

# for i in range(1, min(num1, num2) + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print("GCD =", gcd)



# 2: Using Euclid's Algorithm (Best Method)
# Logic

# Repeat until second number becomes 0.

# GCD(a, b)

# while b != 0
#     a, b = b, a % b

# Answer = a

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# while num2 != 0:
#     num1, num2 = num2, num1 % num2

# print("GCD =", num1)

# _______________________________________________________________

# 2. LCM (Least Common Multiple)
# The LCM of two numbers is the smallest positive number that is divisible by both numbers.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# maximum = max(num1, num2)

# while True:
#     if maximum % num1 == 0 and maximum % num2 == 0:
#         print("LCM =", maximum)
#         break
#     maximum += 1