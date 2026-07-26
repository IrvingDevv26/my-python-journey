# Twenty-eighth program: Print the multiplication table of a number given by
# the user, from 1 to 10, showing each operation and its result.

number = int(input("Introduce the number for the multiplication table: "))

for i in range(1, 11):
    print(f"{number} x {i} =", number * i)
