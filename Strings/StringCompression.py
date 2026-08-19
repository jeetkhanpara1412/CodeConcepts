# Given a string, compress it by replacing consecutive repeated characters with the character followed by its count.

# Input:
# aaabbccccd
# Output:
# a3b2c4d1

# 1: Using a Loop (Most Asked in Interviews)
string = input("Enter a string: ")
compressed = ""
count = 1

for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1

print("Compressed String:", compressed)


# 2: Using while Loop

# string = input("Enter a string: ")
# compressed = ""
# i = 0

# while i < len(string):
#     count = 1

#     while i + 1 < len(string) and string[i] == string[i + 1]:
#         count += 1
#         i += 1

#     compressed += string[i] + str(count)
#     i += 1

# print(compressed)