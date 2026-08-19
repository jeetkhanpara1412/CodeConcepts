# Insertion Sort is a simple sorting algorithm that builds the sorted array one element at a time. It works similarly to how you arrange playing cards in your hand.


# Index : 0   1   2   3
# Value : 7   4   5   2

# Pass 1
# Index : 0   1   2   3
# Value : 4   7   5   2

# Pass 2
# Index : 0   1   2   3
# Value : 4   5   7   2

# Pass 3
# Index : 0   1   2   3
# Value : 2   4   5   7



arr = [7, 4, 5, 2]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)
