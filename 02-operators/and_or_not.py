# Fifteenth program: use logical operators to check whether the user can drive.

age = int(input('Please enter your age: '))
license_answer = int(input('Type [1] if you have a license or [0] if you do not: '))
has_license = license_answer == 1

if age >= 18 and has_license:
    print('You can drive.')
else:
    print('You cannot drive.')
