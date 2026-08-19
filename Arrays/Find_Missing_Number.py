# You are given an array containing n-1 distinct numbers from 1 to n. One number is missing. Your task is to find the missing number.

# arr = [1, 2, 4, 5]
# n = 5
# Output:3

# 1: Using Sum Formula
# n(n+1)/2
arr = [1, 2, 4, 5]
n = 5

expected_sum = n * (n + 1) // 2 #15
actual_sum = sum(arr) #12

missing_number = expected_sum - actual_sum
print("The missing number is:", missing_number) #3


# 2: Using a Loop
arr = [1, 2, 4, 5]
n = 5

missing = 0

for i in range(1, n + 1):
    if i not in arr:
        missing = i
        break

print("Missing Number:", missing)



# 3: Using XOR
arr = [1, 2, 4, 5]
n = 5

xor1 = 0
xor2 = 0

# XOR from 1 to n
for i in range(1, n + 1):
    xor1 ^= i

# XOR of array
for num in arr:
    xor2 ^= num

missing = xor1 ^ xor2

print("Missing Number:", missing)