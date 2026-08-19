# The First Non-Repeated Character problem asks you to find the first character in a string that appears only once.
# 
# Input: "programming"
# Output: "p"

# 1: Using count()
text = input("Enter a string: ")

for char in text:
    if text.count(char) == 1:
        print("First non-repeated character is:", char)
        break
else:
    print("No non-repeated character found.")



# 2: Using Dictionary (Recommended)

# text = input("Enter a string: ")

# frequency = {}

# # Count frequency
# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# # Find first non-repeated character
# for char in text:
#     if frequency[char] == 1:
#         print("First non-repeated character is:", char)
#         break
# else:
#     print("No non-repeated character found.")

