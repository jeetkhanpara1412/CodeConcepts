# Binary Search is a searching algorithm used to find an element in a sorted array.

# Important: Binary Search works only on sorted data.


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 2

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print("Found at index = ", mid,"\ntargrt is =", target)
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

else:
    print("Not Found")