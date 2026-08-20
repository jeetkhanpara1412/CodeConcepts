# Selection Sort is a simple sorting algorithm that repeatedly finds the smallest element from the unsorted part of the array and places it at the beginning.

# arr = [64, 25, 12, 22, 11]
# [64, 25, 12, 22, 11]

# 1: simple 
arr = [64, 25, 12, 22, 11]
n = len(arr)
print(n)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)


# Descending Order
        # if arr[j] > arr[min_index]:
rev = arr[::-1]
print(rev)


