# Seventeenth program: combine logical operators to decide if you can get on a ride.

height = int(input('Please enter your height (in cm): '))
age = int(input('Now enter your age: '))
accompanied_answer = int(input('Type [1] if you are accompanied by an adult or [0] if not: '))
is_accompanied = accompanied_answer == 1

# The rule: be at least 140 cm tall AND (be 12 or older OR be accompanied by an adult).
if height >= 140 and (age >= 12 or is_accompanied):
    print('You can get on.')
else:
    print('You cannot get on.')
