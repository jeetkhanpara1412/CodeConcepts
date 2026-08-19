# Given an array of n+1 integers where each integer is in the range 1 to n, find the duplicate number.

# Input: [1, 3, 4, 2, 2]
# Output: 2


# 1: Using Nested Loops
arr = [1, 3, 4, 2, 2]
duplicate = -1

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            duplicate = arr[i]
            break

    if duplicate != -1:
        break

print("Duplicate Number:", duplicate)




# 2: Using Hash Set

arr = [1, 3, 4, 2, 2]

seen = set()

for num in arr:
    if num in seen:
        print("Duplicate Number:", num)
        break
    seen.add(num)



# 3: Using Sorting
arr = [1, 3, 4, 2, 2]

arr.sort()

for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        print("Duplicate Number:", arr[i])
        break

