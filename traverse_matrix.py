# Forty-sixth program: Given a matrix (a list of lists), traverse it with two
# nested loops and compute: (a) the sum of all its elements, (b) the sum of
# each row separately, (c) the largest value in the whole matrix along with
# its [row][column] position. The outer loop moves through the rows and the
# inner loop through the columns of the current row.

matrix = [[3, 8, 1], [9, 2, 7], [4, 6, 5]]

total_sum = 0
# Start the maximum at the very first cell (0,0) so the first comparison is
# always against a real number, never None.
max_value = matrix[0][0]
max_row = 0
max_column = 0
for row in range(len(matrix)):
    row_sum = 0
    for column in range(len(matrix[row])):
        value = matrix[row][column]
        if value > max_value:
            max_value = value
            max_row = row
            max_column = column
        total_sum += value
        row_sum += value
    print(f"Sum of row {row}:", row_sum)

print("Max value:", max_value, f"at [{max_row}][{max_column}]")
print("Total sum:", total_sum)
