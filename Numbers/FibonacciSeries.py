# A Fibonacci Series is a sequence of numbers where each number is the sum of the previous two numbers.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Formula
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)

# 1: Using a for Loop (Most Common)

n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c 


# 2: Using a while Loop

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1
# count = 0

# while count < n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     count += 1

