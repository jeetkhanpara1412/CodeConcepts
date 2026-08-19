# Character Frequency means counting how many times each character appears in a string.

# Input:
# hello
# Output:
# h : 1
# e : 1
# l : 2
# o : 1

# 1: Using Dictionary (Most Common)

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:")
for char, count in frequency.items():
    print(char, ":", count)


# 2: Using count() Function
# text = input("Enter a string: ")
# for char in set(text):
#     print(char, ":", text.count(char))

