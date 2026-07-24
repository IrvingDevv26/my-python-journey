# Forty-fifth program: Print an 8x8 chessboard, alternating [#] for black
# squares and [ ] for white ones. The trick is the parity of (row + column):
# when that sum is even the square is one color, when it's odd it's the other.
# Because each step in a row and each new row flips the parity, the colors
# alternate correctly in both directions, just like a real chessboard.

for row in range(8):
    for column in range(8):
        if (row + column) % 2 == 0:
            print("[#]", end=" ")
        else:
            print("[ ]", end=" ")
    print()
