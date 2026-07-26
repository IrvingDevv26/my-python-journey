# Fifty-sixth program: Loop through a list of words with enumerate and decide
# which ones are palindromes (they read the same forwards and backwards). To
# check, compare each word with its reversed version, rebuilt with
# "".join(reversed(word)): reversed gives the letters back to front and join
# glues them into a string again. Show the position and result of each word,
# and how many palindromes there are at the end.

words = ["reconocer", "python", "anilina", "hola", "somos", "arte"]

count = 0
for position, word in enumerate(words, start=1):
    reversed_word = "".join(reversed(word))
    if word == reversed_word:
        result = "is a palindrome"
        count += 1
    else:
        result = "is not a palindrome"
    print(f"{position}. {word} {result}")

print(f"\nTotal palindromes: {count}")
