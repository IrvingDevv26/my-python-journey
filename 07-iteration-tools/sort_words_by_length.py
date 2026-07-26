# Fifty-third program: Display a list of words sorted by length (shortest to
# longest) and, for each word, print how many letters it has. sorted with
# key=len tells Python to compare the words by their length instead of
# alphabetically.

words = ["python", "es", "un", "lenguaje", "genial", "para", "aprender"]

for word in sorted(words, key=len):
    print(f"{word}: {len(word)} letters")
