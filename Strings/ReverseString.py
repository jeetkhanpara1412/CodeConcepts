# Reversing a string means changing the order of its characters from last to first

# 1: Using Slicing (Most Common)

# text = "Python"

# reverse = text[::-1]

# print("Original String:", text)
# print("Reversed String:", reverse)


# 2: Using a for Loop

text = "Python"

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed String:", reverse)



# 3: Using reversed() Function

# text = "Python"

# reverse = "".join(reversed(text))

# print(reverse)



# 4: Using while Loop

# text = "Python"

# reverse = ""
# i = len(text) - 1

# while i >= 0:
#     reverse += text[i]
#     i -= 1

# print(reverse)

