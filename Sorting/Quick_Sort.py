# Quick Sort is one of the fastest sorting algorithms. It uses the Divide and Conquer technique.

def partition(arr, low, high):
    pivot = arr[high]          # Last element as pivot
    i = low - 1                # Index of smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


arr = [7, 2, 1, 6, 8, 5, 3, 4]

quick_sort(arr, 0, len(arr) - 1)

print(arr)