# Twenty-fifth program: Ask the user for a number and print every number from
# 1 up to that number (inclusive). A simple counting-up loop using range.

number_ends = int(input("Please introduce a number that you want to end print: "))

for i in range(1, number_ends + 1):
    print(i)
