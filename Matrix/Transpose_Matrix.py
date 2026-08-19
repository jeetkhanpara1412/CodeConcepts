# The Transpose of a Matrix means converting all rows into columns and all columns into rows.

# 1 2 3
# 4 5 6

# 1 4
# 2 5
# 3 6

# 1: Using Nested Loops

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
cols = len(matrix[0])

tanspose = []

for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    tanspose.append(row)

print(tanspose)



# 2: Using zip()
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = list(map(list, zip(*matrix)))

print(transpose)



# 3: Using List Comprehension

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(transpose)

