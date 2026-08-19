# Given an array and an integer k, find the maximum sum of any contiguous subarray of size k.

# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# [2,1,5] = 8
# [1,5,1] = 7
# [5,1,3] = 9
# [1,3,2] = 6

# Maximum Sum =  answer = 9

arr = [2, 1, 5, 1, 3, 2]
k = 3

for i in range(len(arr) - k + 1):
    current_sum = sum(arr[i:i+k])
    if i == 0:
        max_sum = current_sum
    else:
        max_sum = max(max_sum, current_sum)

print(max_sum)



arr = [2, 1, 5, 1, 3, 2]
k = 3

# Step 1: Calculate the first window sum
window_sum = sum(arr[:k])

# Step 2: Store it as the current maximum
max_sum = window_sum

# Step 3: Slide the window
for i in range(k, len(arr)):

    # Remove left element
    window_sum -= arr[i - k]

    # Add new right element
    window_sum += arr[i]

    # Update maximum
    max_sum = max(max_sum, window_sum)

print(max_sum)