# Forty-seventh program: Build a matrix of 3 rows x 4 columns with loops, where
# each element equals row * 4 + column. Print it as a grid. Then build its
# transpose (4 rows x 3 columns), where the original element at [i][j] moves to
# position [j][i], and print that too. To transpose, the new outer loop walks
# the original columns and the inner loop walks the original rows.

rows = 3
columns = 4

# Build the original 3x4 matrix
matrix = []
for row in range(rows):
    new_row = []
    for column in range(columns):
        new_row.append(row * 4 + column)
    matrix.append(new_row)

# Print the original matrix as a grid (:4 keeps the columns aligned)
print("---Original matrix (3x4)---")
for row in range(rows):
    for column in range(columns):
        print(f"{matrix[row][column]:4}", end=" ")
    print()

# Build the transpose: the outer loop now goes over the original columns, so
# each original column becomes a row of the new matrix.
transpose = []
for column in range(columns):
    new_row = []
    for row in range(rows):
        new_row.append(matrix[row][column])
    transpose.append(new_row)

# Print the transposed matrix (4x3)
print("\n---Transposed matrix (4x3)---")
for row in range(columns):
    for column in range(rows):
        print(f"{transpose[row][column]:4}", end=" ")
    print()
