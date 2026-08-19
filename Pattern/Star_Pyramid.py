# The Star Pyramid is one of the most common beginner programming patterns. It helps you understand:

# For n = 5

#     *
#    ***
#   *****
#  *******
# *********

n = 5

for i in range(n):
    print(' ' * (n - i - 1) + '.' * (2 * i + 1))

#  2: Using Nested Loops

# Instead of string multiplication, you can print the pattern using nested loops.

n = 5

for i in range(1, n + 1):

    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")

    print() 