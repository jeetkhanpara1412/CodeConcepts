# Given an array (list) of elements, remove all duplicate elements so that each element appears only once.

# arr = [1, 2, 2, 3, 4, 4, 5]
# [1, 2, 3, 4, 5]



# 1: Using set() (Simplest)
# arr = [1, 2, 2, 3, 4, 4, 5]
# result = list(set(arr))
# print(result)


# 2: Using a Loop (Maintains Order) ⭐ Most Asked in Interviews

# arr = [1, 2, 2, 3, 4, 4, 5]
# result = []

# for i in arr:
#     if i not in result:
#         result.append(i)

# print(result)

arr = [1, 2, 2, 3, 4, 4, 5]
result = []

for i in arr:
    if i not in result:
        result.append(i)

print(result)

