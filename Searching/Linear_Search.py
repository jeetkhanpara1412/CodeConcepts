# Linear Search is the simplest searching algorithm. It checks each element of the array one by one until it finds the target element or reaches the end of the array.


arr = [12, 45, 7, 23, 56]
target = 23

found = -1

for i in range(len(arr)):
    if arr[i] == target:
        found = i
        break

if found != -1:
    print("Element found at index", found)
else:
    print("Element not found")
    
     