# Bubble Sort is one of the simplest sorting algorithms. It repeatedly compares two adjacent elements and swaps them if they are in the wrong order.

# arr = [5, 3, 8, 4, 2]
# [2, 3, 4, 5, 8]


# 1: Simple

arr = [5, 3, 8, 4, 2]

n = len(arr)

for i in range(n):
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j] # swap the values

print(arr)


# 2: Optimized Bubble Sort

arr = [5, 3, 8, 4, 2]
n = len(arr)

for i in range(n):
    swapped = False
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break

print(arr)


