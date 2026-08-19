# Find the largest (maximum) element from a list of numbers.

# Input: [10, 25, 8, 45, 12]
# Output: 45

# 1: Using Loop (Interview Method)

number = [1,5,6,7,8,10]
lagest = number[0]

for i in number:
    if i > lagest:
        lagest = i

print(lagest)  # Output: 10


# 2: Using max() Function

# number = [1,5,6,7,8,10]
# print(max(number))  # Output: 10



# 3: Using sort() Function

# number = [1,5,6,7,8,10]
# number.sort()
# print(number[-1])  # Output: 10
