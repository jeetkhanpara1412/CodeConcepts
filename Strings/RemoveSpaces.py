# Removing spaces means deleting whitespace characters from a string. Python provides several ways to do this depending on your requirement.

# 1: Using replace() (Most Common)

text = "Hello World"
result = text.replace(" ", "")
print(result)


# 2: Remove Leading and Trailing Spaces (strip())
# text = "   Python Programming   "
# result = text.strip()
# print(result)


# 3: Remove Only Left Spaces (lstrip())
# text = "     Hello"
# print(text.lstrip())


# 4: Remove Only Right Spaces (rstrip())
# text = "Hello     "
# print(text.rstrip())


# 5: Remove All Whitespace (split() + join())
# text = "Hello   World   Python"
# result = "".join(text.split())
# print(result)


# 6: Using List Comprehension
# text = "Hello World"
# result = "".join([ch for ch in text if ch != " "])
# print(result)