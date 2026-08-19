# A Palindrome String is a string that reads the same forward and backward.

# level	level	✅ Yes
# python	nohtyp	❌ No

# 1: Using String Slicing (Recommended)

# str = input("enter string:")

# if str == str[::-1]:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")



# 2: using loop 

string = input("Enter a string: ")

reverse = ""

for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("Palindrome String")
else:
    print("Not a Palindrome String")


# 3: Using reversed()

# string = input("Enter a string: ")

# reverse = "".join(reversed(string))

# if string == reverse:
#     print("Palindrome String")
# else:
#     print("Not a Palindrome String")


