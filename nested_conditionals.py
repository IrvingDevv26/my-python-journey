# Sixteenth program: use nested conditionals to check if the user can watch a movie.

age = int(input('Enter your age: '))

if age < 18:
    accompanied_answer = int(input('Are you accompanied by an adult? [1] Yes [0] No: '))
    is_accompanied = accompanied_answer == 1
    if is_accompanied:
        print('You can watch the movie.')
    else:
        print('You cannot watch the movie.')
else:
    print('You can watch the movie.')
