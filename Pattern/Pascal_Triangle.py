# What is Pascal Triangle?

# Pascal Triangle is a triangular arrangement of numbers where:

# The first row contains 1.
# Every row starts and ends with 1.
# Every middle number is the sum of the two numbers directly above it.

# Example (first 6 rows):

#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1
# 1  5  10 10  5  1


# 1 Using Lists

n = 5

triangle = []

for i in range(n):

    row = [1] * (i + 1)

    for j in range(1, i):

        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    triangle.append(row)

for row in triangle:
    print(row)



# 2 Using Combination Formula

from math import factorial

n = 5

for i in range(n):

    for j in range(i + 1):

        value = factorial(i) // (factorial(j) * factorial(i - j))

        print(value, end=" ")

    print()