# Eighteenth program: use the 'in' operator to check if a letter is a vowel.

vowels = 'aeiou'
letter = input('Type a letter: ')

if letter in vowels:
    print(f'The letter {letter} is a vowel.')
else:
    print(f'The letter {letter} is a consonant.')
