# Twenty-first program: use the string methods len(), strip(), upper() and lower().

phrase = '    HeLlo WoRLd    '
clean_phrase = phrase.strip()

print('The original phrase is:', phrase)
print('The phrase without leading and trailing spaces is:', clean_phrase)
print('The phrase in uppercase is:', clean_phrase.upper())
print('The phrase in lowercase is:', clean_phrase.lower())
print('The length of the phrase is:', len(clean_phrase))
