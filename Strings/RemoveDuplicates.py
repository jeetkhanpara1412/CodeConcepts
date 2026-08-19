# Removing duplicates means eliminating repeated elements from a string, list, or other collection while keeping only unique values.

# 1. Remove Duplicates from a List (Using set())

# numbers = [10, 20, 10, 30, 20, 40]
# unique = list(set(numbers))
# print(unique)


# 2. Remove Duplicates While Preserving Order (Recommended)

# numbers = [10, 20, 10, 30, 20, 40]
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)


# 3. Remove Duplicate Characters from a String

text = "programming"
result = ""
for ch in text:
    if ch not in result:
        result += ch

print(result)