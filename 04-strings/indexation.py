# Twenty-third program: access individual characters of a string by their index.

word = input('Please enter a word: ')
middle_position = len(word) // 2

print('The first letter is:', word[0])
print('The last letter is:', word[-1])
print('The middle letter is:', word[middle_position])
