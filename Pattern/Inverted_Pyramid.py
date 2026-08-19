# Inverted Pyramid Pattern in Python

# An Inverted Pyramid is a star (*) pattern where:

# The first row has the maximum number of stars.
# The number of stars decreases by 2 in each row.
# The leading spaces increase by 1 in each row.
# The pattern looks like an upside-down pyramid.

# Example (n = 5)
# *********
#  *******
#   *****
#    ***
#     *


n = 5 

for i in range(n):
    print(' ' * i, end='')

    print('^' * (2 * (n - i) - 1)) 



# 2:Using Nested Loops

n = 5

for i in range(n):
    for j in range(i):
        print(' ', end='')

    for j in range(2 * (n - i) - 1):
        print('^', end='')

    print()

