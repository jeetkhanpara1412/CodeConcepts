# Given a list of numbers, find the second largest unique element.

# numbers = [10, 20, 5, 8, 20, 15]
# Output: 15

# 1: Using sort() (Easy)

numbers = [4, 1, 7, 3, 7, 2, 5, 4]
sorted_numbers = list(set(numbers))  # Remove duplicates and convert back to list
sorted_numbers.sort()  # Sort the list in ascending order
print("Second largest is = ", sorted_numbers[-2])



# 2: Without Sorting (Best for Interviews)

numbers = [4, 1, 7, 3, 7, 2, 5, 4]
largest = second_largest = float('-inf')  # Initialize to negative infinity

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    else:
        if largest > i > second_largest:
            second_largest = i


print("Second largest is = ", second_largest)


# 3: Using max()
numbers = [10, 20, 5, 8, 20, 15]
largest = max(numbers)

numbers.remove(largest)
second_largest = max(numbers)

print("second_largest is = ", second_largest)