# 153
# 1³ + 5³ + 3³
# = 1 + 125 + 27
# = 153  equal to 153 so it is Armstrong Number
 
# 9474
# 9⁴ + 4⁴ + 7⁴ + 4⁴
# = 6561 + 256 + 2401 + 256
# = 9474  equal to 9474 so it is Armstrong Number

# 123
# 1³ + 2³ + 3³
# = 1 + 8 + 27
# = 36   Not equal to 123 so it is NOT Armstrong Number


num = int(input("Enter a number: "))

original = num
power = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** power
    num = num // 10

if sum == original:
    print(original, "is an Armstrong Number")
else:
    print(original, "is NOT an Armstrong Number")
    