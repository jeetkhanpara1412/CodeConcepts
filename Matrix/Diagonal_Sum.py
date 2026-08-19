# The Diagonal Sum problem asks you to find the sum of the elements on the main diagonal and secondary diagonal of a square matrix.

# For matrices with an odd size (3×3, 5×5, etc.), the center element belongs to both diagonals, so it should be counted only once.


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)
total = 0

for i in range(n):
    # Main diagonal
    total += matrix[i][i]

    # Secondary diagonal
    total += matrix[i][n - i - 1]

# Remove duplicate center element
if n % 2 == 1:
    total -= matrix[n // 2][n // 2]

print("Diagonal Sum =", total)

