# Given an array of size n, find the element that appears more than n/2 times.

# nums = [2,2,1,1,1,2,2]
# 2
# Length = 7
# n/2 = 3.5
# 2 appears 4 times
# 4 > 3.5
# Answer = 2


nums = [2,2,1,1,1,2,2]

count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for key in count:
    if count[key] > len(nums) / 2:
        print(key)
        break



# Shorter Python Code

for num in nums:
    count[num] = count.get(num, 0) + 1

for key, value in count.items():
    if value > len(nums) / 2:
        print(key)
        break