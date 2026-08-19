# The Sum of Digits program calculates the total of all digits in a given number.

# 1234
# 1 + 2 + 3 + 4 = 10


# 1: Using while Loop

num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits =", sum)


# 2: Using for Loop
# num = input("Enter a number: ")

# sum = 0

# for digit in num:
#     sum = sum + int(digit)

# print("Sum of digits =", sum)



# 3: Using sum() Function
# num = input("Enter a number: ")
# result = sum(int(digit) for digit in num)
# print("Sum of digits =", result)

