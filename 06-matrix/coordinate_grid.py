# Forty-first program: Using two nested loops, print a grid of 4 rows by 6
# columns where each position displays its coordinates in the format
# (row,column). The outer loop handles the rows and the inner loop handles the
# columns; end=" " keeps a row on one line and the empty print() breaks to the
# next row.

for row in range(4):
    for column in range(6):
        print(f"({row},{column})", end=" ")
    print()
