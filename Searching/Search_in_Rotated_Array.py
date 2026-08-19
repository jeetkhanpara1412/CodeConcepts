# You are given a sorted array that has been rotated at some pivot.

# Original:
# [1, 2, 3, 4, 5, 6, 7]

# Rotated:
# [4, 5, 6, 7, 1, 2, 3]

def search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

arr = [4,5,6,7,1,2,3]

print(search(arr,3))