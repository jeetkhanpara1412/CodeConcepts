# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

# nums = [2, 7, 11, 15]
# target = 9

# [0, 1]

# nums[0] + nums[1]
# 2 + 7 = 9

nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break



# using a hash map (dictionary) to store the indices of the numbers we have seen so far, we can solve this problem in a more efficient way. Here's an implementation:

nums = [2, 7, 11, 15]
target = 9

hash_map = {}

for i in range(len(nums)):
    complement = target - nums[i]
    # print(f"Current number: {nums[i]}, Complement: {complement}")
    if complement in hash_map:
        print([hash_map[complement], i])
        break
    hash_map[nums[i]] = i

