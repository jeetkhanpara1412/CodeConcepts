# A Palindrome Number is a number that reads the same forward and backward.

# 12321	12321	✅ Yes
# 123	321	❌ No

# 1
num = int(input("Enter a number: "))

orignal_num = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if orignal_num == reverse:
    print(f"{orignal_num} is a Palindrome Number ✅ Yes")
else:
    print(f"{orignal_num} is not a Palindrome Number ❌ No")


# 2
# Using String Slicing 
# num = input("Enter a number: ")

# if num == num[::-1]:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")


# 3
# num = input("Enter a number: ")

# reverse = ''.join(reversed(num))

# if num == reverse:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")