# Forty-second program: Ask the user for a number n and display the
# multiplication tables from 1 to n, each one running from 1 to 10. The outer
# loop picks which table to print and the inner loop builds that table. Each
# table has a header and is separated from the next by a blank line.

n = int(input("Enter the last number: "))

for table in range(1, n + 1):
    print(f"---Multiplication table {table}---")
    for multiplier in range(1, 11):
        print(f"{table} x {multiplier} =", table * multiplier)
    print()
