# Thirtieth program: Ask the user for a word and print it reversed. Each new
# character is placed in front of the accumulated result, so the string ends
# up built from back to front.

word = input("Introduce the word: ")
result = ""
for i in word:
    result = i + result

print(f"Reversed word: {result}")
