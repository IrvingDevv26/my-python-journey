# Forty-third program: Print a 10x10 Pythagorean (multiplication) table where
# each cell contains the product of its row and column, neatly aligned in
# columns. It has a header row and a header column with the numbers from 1 to
# 10. Alignment is done with f"{value:4}", which pads every number to a width
# of 4 characters so the columns line up no matter how many digits the number
# has.

# Header row: an empty corner (4 spaces) followed by the numbers 1 to 10
print(f"{'':4}", end=" ")
for column in range(1, 11):
    print(f"{column:4}", end=" ")
print()

# Table body: each row starts with its header number, then the products
for row in range(1, 11):
    print(f"{row:4}", end=" ")
    for column in range(1, 11):
        print(f"{row * column:4}", end=" ")
    print()
