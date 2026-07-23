# Thirty-fourth program: Ask the user for a number between 1 and 10. If they
# enter something outside that range, show an error message and ask again as
# many times as needed until the value is valid. The while loop repeats while
# the number is out of range, so it only ends when the input is correct.

number = int(input("Enter a number between 1 and 10: "))
while number < 1 or number > 10:
    print("Number out of range")
    number = int(input("Please enter a number between 1-10: "))
print(f"Valid number: {number}")
