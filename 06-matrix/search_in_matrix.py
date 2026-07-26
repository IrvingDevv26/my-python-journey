# Forty-eighth program: Given a matrix of numbers, ask the user for a value and
# search for it by traversing the matrix. If found, show its [row][column]
# position and stop both loops. If not found, report that it doesn't exist.
# Also count how many comparisons were made before finding it. A "found" flag
# lets the outer loop know it can also stop after the inner loop breaks.

matrix = [[3, 8, 1, 5], [9, 2, 7, 6], [4, 6, 5, 0]]
target = int(input("Enter the value you want to search for: "))

found = False
comparisons = 0
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        comparisons += 1
        if matrix[row][column] == target:
            found = True
            break
    # If the inner loop found the value and broke out, stop the outer loop too
    if found:
        break

if found:
    print(f"Value {target} found at [{row}][{column}]")
else:
    print(f"Value {target} isn't in the matrix")
print("Comparisons made:", comparisons)
