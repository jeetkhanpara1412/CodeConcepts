# Count Vowels means finding how many vowels (a, e, i, o, u) are present in a given string.

# Input  : Hello World
# Output : 3

# 1: Using a Loop (Best for Beginners)
 
text = input("Enter a string: ")

count = 0

for char in text:
    if char.lower() in 'aeiou':
        count += 1

print("Number of vowels:", count)


# 2: Using sum()

# text = input("Enter a string: ")
# count = sum(1 for ch in text if ch.lower() in "aeiou")
# print("Number of vowels:", count)


# 3: Using a List

# text = input("Enter a string: ")

# vowels = []

# for ch in text:
#     if ch.lower() in "aeiou":
#         vowels.append(ch)

# print("Vowels:", vowels)
# print("Count:", len(vowels))

