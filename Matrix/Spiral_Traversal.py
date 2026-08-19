# What is Spiral Traversal?

# Spiral Traversal (also called Spiral Order or Clockwise Matrix Traversal) is the process of printing all elements of a matrix in a spiral pattern.

# Instead of reading row by row, we move:

# ➡️ Left to Right
# ⬇️ Top to Bottom
# ⬅️ Right to Left
# ⬆️ Bottom to Top

# Then repeat the same process for the remaining inner matrix.

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1

result = []

while top <= bottom and left <= right:

    # Left -> Right
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    # Top -> Bottom
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    # Right -> Left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    # Bottom -> Top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(result)