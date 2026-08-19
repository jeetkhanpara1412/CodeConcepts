# Matrix Addition is one of the most basic matrix operations. It means adding two matrices of the same size element by element.

# A matrix is simply a 2D list (list of lists) in Python.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# ROULS Two matrices can be added only if they have the same number of rows and columns.

# 1+7   2+8   3+9
# 4+1   5+2   6+3

# 8 10 12
# 5  7  9


# 1 Using Nested Loops
A = [[1,2,3],[4,5,6]]
B = [[1,2,3],[4,5,6]]

result = []

for i in range(len(A)):
    row = []

    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])

    result.append(row)

print(result)



# 2 List Comprehension
A = [[1, 2],[3, 4]]
B = [[5, 6],[7, 8]]

result = [
    [A[i][j] + B[i][j] for j in range(len(A[0]))]
    for i in range(len(A))
]

print(result)



# 3 Using NumPy

import numpy as np

A = np.array([[1,2],[3, 4]])
B = np.array([[5, 6],[7, 8]])

print(A+B)