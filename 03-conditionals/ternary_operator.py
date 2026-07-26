# Nineteenth program: use a ternary operator to tell whether a number is even or odd.

number = int(input('Please enter the number: '))
print(f'The number {number} is even' if number % 2 == 0 else f'The number {number} is odd')
