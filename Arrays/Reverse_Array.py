# Reverse Array means arranging the elements of an array (or list in Python) in the opposite order.

# Original Array: [10, 20, 30, 40, 50]
# Reversed Array: [50, 40, 30, 20, 10]

# 1: Using reverse() (Inbuilt Method)
arr = [10, 20, 30, 40, 50]
arr.reverse()
print("Reversed Array:", arr)


# 2: Using Slicing

arr = [10, 20, 30, 40, 50]
reversed_arr = arr[::-1]

print("Original Array:", arr)
print("Reversed Array:", reversed_arr)

# 3: Using reversed()
arr = [10, 20, 30, 40, 50]
reversed_arr = list(reversed(arr))
print(reversed_arr)



# 4: Using a Loop
arr = [10, 20, 30, 40, 50]
reverse = []
for i in range(len(arr)-1, -1, -1):
    reverse.append(arr[i])

print("Reversed Array:", reverse)




# 5: Reverse Using Two Pointers
arr = [10, 20, 30, 40, 50]
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)