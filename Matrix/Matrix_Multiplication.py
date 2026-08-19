# Matrix multiplication is one of the most important operations in mathematics, data science, machine learning, computer graphics, and engineering.

# Matrix Multiplication means multiplying two matrices by taking the dot product of rows and columns.


# A = 2 × 3
# B = 3 × 2

# ✔ Multiplication is possible
# Result = 2 × 2 matrix


# A = 2 × 3
# B = 2 × 3

# ❌ Multiplication is not possible


A = [[1, 2],[3, 4]]
B = [[5, 6],[7, 8]]

result = [[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)



# 2: Using NumPy

import numpy as np

A = np.array([[1, 2],[3, 4]])

B = np.array([[5, 6],[7, 8]])

result = np.matmul(A,B)
print(result)