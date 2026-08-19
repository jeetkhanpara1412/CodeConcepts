# Given an array (list) of elements, count how many times each element appears.

# arr = [1, 2, 2, 3, 1, 4, 2]
# 1 : 2
# 2 : 3
# 3 : 1
# 4 : 1


# 1: Using Dictionary
# arr = [1, 2, 2, 3, 1, 4, 2]
# frequency = {}

# for i in arr:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1

# print(frequency)


# 2: Using count()

arr = [1, 2, 2, 3, 1, 4, 2]

for i in arr:
    print(i, ":", arr.count(i))




# 3: Using collections.Counter
from collections import Counter
arr = [1, 2, 2, 3, 1, 4, 2]
frequency = Counter(arr)
print(frequency)