# The Smallest Element problem is used to find the minimum value from a list of numbers.
# numbers = [25, 10, 45, 5, 18]
# 5


# 1: Using min() Function (Built-in)

numbers = [25, 10, 45, 5, 18]
smallest = min(numbers)
print(smallest)


numbers = [25, 10, 45, 5, 18]
numbers.sort()
print(numbers[0])



# 2: Using a Loop

numbers = [25, 10, 45, 5, 18]
smallest = numbers[0] #25

for i in numbers:
    if i < smallest:
        smallest = i 

print(smallest)