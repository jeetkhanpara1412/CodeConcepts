# Given an array and a number k, rotate the array by k positions.

# There are two types of rotation:

# Left Rotation → Elements move to the left.
# Right Rotation → Elements move to the right.

# arr = [1, 2, 3, 4, 5]
# k = 2
# [3, 4, 5, 1, 2]


# 1: Using List Slicing

arr = [1, 2, 3, 4, 5]
k = 2
k = k % len(arr)
rotated = arr[k:] + arr[:k]
print(rotated)  # Output: [3, 4, 5, 1, 2]


# 2: Rotate One by One
arr = [1,2,3,4,5]
k = 2

for i in range(k):
    first = arr.pop(0)
    arr.append(first)

print(arr)


# 3: Without Using Built-in Functions
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1,2,3,4,5]
k = 2

n = len(arr)
k = k % n

reverse(arr, 0, k-1)
reverse(arr, k, n-1)
reverse(arr, 0, n-1)

print(arr)