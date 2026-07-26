# Fourteenth program: use if/elif/else to classify a grade into a letter.

grade = int(input('Enter the grade you got (0-100): '))

if grade >= 90:
    print('You got an A.')
elif grade >= 80:
    print('You got a B.')
elif grade >= 70:
    print('You got a C.')
else:
    print('You did not pass.')
