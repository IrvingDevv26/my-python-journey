# Forty-fourth program: Ask for a height n and print four different star
# patterns, one below the other. Each one plays with how many stars per row
# and how many leading spaces:
#   (a) increasing left-aligned triangle
#   (b) decreasing triangle
#   (c) right-aligned triangle (spaces push the stars to the right)
#   (d) centered pyramid (spaces on the left + an odd number of stars)

height = int(input("Introduce the height of the triangles: "))

print("---Increasing triangle---")
for row in range(1, height + 1):
    for column in range(row):
        print("*", end="")
    print()

print("\n---Decreasing triangle---")
for row in range(height, 0, -1):
    print("*" * row)

print("\n---Right-aligned triangle---")
for row in range(1, height + 1):
    for space in range(height - row):
        print(" ", end="")
    for asterisk in range(row):
        print("*", end="")
    print()

print("\n---Centered pyramid---")
for row in range(1, height + 1):
    print(" " * (height - row) + "*" * (2 * row - 1))
