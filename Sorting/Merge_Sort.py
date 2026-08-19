# Merge Sort is a Divide and Conquer algorithm.

# It works in 3 steps:

# Divide the array into two halves.
# Sort each half recursively.
# Merge the two sorted halves into one sorted array.

# arr = [8, 3, 5, 4, 7, 6, 1, 2]
#                 [8,3,5,4,7,6,1,2]
#                 /               \
#          [8,3,5,4]           [7,6,1,2]
#          /      \            /       \
#      [8,3]    [5,4]      [7,6]     [1,2]
#      /   \     /   \      /   \      /   \
def merge_sort(arr):
    if len(arr) > 1:

        # Find middle index
        mid = len(arr) // 2          # = 4

        # Divide array into two halves
        left = arr[:mid]             # = [8, 3, 5, 4]
        right = arr[mid:]            # = [7, 6, 1, 2]

        # Recursively sort left half
        merge_sort(left)             # [8,3] -> [8],[3] -> [3,8]
                                     # [5,4] -> [5],[4] -> [4,5]
                                     # Final Left = [3,4,5,8]

        # Recursively sort right half
        merge_sort(right)            # [7,6] -> [7],[6] -> [6,7]
                                     # [1,2] -> [1],[2] -> [1,2]
                                     # Final Right = [1,2,6,7]

        # Initialize pointers
        i = j = k = 0
        # i = left index
        # j = right index
        # k = original array index

        # Merge two sorted arrays
        while i < len(left) and j < len(right):    # True (0<4 and 0<4)

            if left[i] < right[j]:         # 3 < 1 ? False
                arr[k] = left[i]           # Copy left element
                i += 1                     # Move left pointer
            else:
                arr[k] = right[j]          # arr[0] = 1
                j += 1                     # Move right pointer

            k += 1                         # Move array pointer

        # Copy remaining left elements
        while i < len(left):
            arr[k] = left[i]                # Copy remaining left values
            i += 1
            k += 1

        # Copy remaining right elements
        while j < len(right):
            arr[k] = right[j]               # Copy remaining left values
            j += 1
            k += 1


arr = [8, 3, 5, 4, 7, 6, 1, 2]

merge_sort(arr)

print(arr)                                  # [1, 2, 3, 4, 5, 6, 7, 8]
