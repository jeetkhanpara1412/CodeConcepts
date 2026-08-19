# Given an array of integers, move all the 0s to the end of the array while maintaining the relative order of the non-zero elements.

# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# 1: Using Extra List
arr = [0, 1, 0, 3, 12]

result = []

for num in arr:
    if num != 0:
        result.append(num)

zeros = len(arr) - len(result)

result.extend([0] * zeros)

print(result)


# 2: Using sort()
arr = [0, 1, 0, 3, 12]
arr.sort(key=lambda x: x == 0)
print(arr)



# Interview Solution
arr = [0, 1, 0, 3, 12]
index = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[index], arr[i] = arr[i], arr[index]
        index += 1

print("After moving zeros:", arr)