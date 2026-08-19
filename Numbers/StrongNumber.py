# A Strong Number is a number in which the sum of the factorials of its digits is equal to the original number.
# 40585	4! + 0! + 5! + 8! + 5! = 40585	✅ Yes
# 123	1! + 2! + 3! = 9	❌ No


# 1 Using math.factorial()

import math 

num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum += math.factorial(digit)
    num //= 10

if sum == original:
    print("Strong Number")
else:
    print("Not Strong Number")



# 2 Without Using math.factorial()

# num = int(input("Enter a number: "))

# original = num
# sum = 0

# while num > 0:
#     digit = num % 10

#     # Find factorial
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i

#     sum += fact
#     num //= 10

# if sum == original:
#     print("Strong Number")
# else:
#     print("Not Strong Number")
