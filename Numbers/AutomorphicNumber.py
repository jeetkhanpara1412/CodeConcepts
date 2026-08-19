# An Automorphic Number is a number whose square ends with the same number.

# 5 = 25 _/
# 7 = 49 x

# 1 Without Using String (Interview Method)
num = int(input("Enter a number: "))

square = num * num

digits = len(str(num))

last_digits = square % (10 ** digits)

if last_digits == num:
    print(num, "is an Automorphic Number")
else:
    print(num, "is NOT an Automorphic Number")



# 2 Using String
# num = int(input("Enter a number: "))

# square = num * num

# if str(square).endswith(str(num)):
#     print(num, "is an Automorphic Number")
# else:
#     print(num, "is NOT an Automorphic Number")


# 3 Without len() and Without String
# num = int(input("Enter a number: "))
# square = num * num
# temp = num
# digits = 0

# while temp > 0:
#     digits += 1
#     temp //= 10

# last_digits = square % (10 ** digits)

# if last_digits == num:
#     print(num, "is an Automorphic Number")
# else:
#     print(num, "is NOT an Automorphic Number")