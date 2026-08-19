# Given an array and a target sum, count how many pairs have a sum equal to the target.

# arr = [1, 5, 7, -1, 5]
# target = 6
# Possible pairs:
# (1, 5)
# (7, -1)
# (1, 5)   # second 5
# Output = 3

arr = [1, 5, 7, -1, 5]
target = 6

count = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            # print(f"Pair found: ({arr[i]}, {arr[j]})")
            count += 1

print(count)






arr = [1, 5, 7, -1, 5]
target = 6

hashmap = {}
count = 0

for num in arr:

    complement = target - num

    if complement in hashmap:
        count += hashmap[complement]

    if num in hashmap:
        hashmap[num] += 1
    else:
        hashmap[num] = 1

print(count)