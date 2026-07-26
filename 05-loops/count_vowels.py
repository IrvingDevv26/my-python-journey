# Twenty-ninth program: Ask the user for a word and count how many vowels it
# contains. It goes through each character and checks if it belongs to the
# group of vowels (both lowercase and uppercase).

vowels = "aeiouAEIOU"
word = input("Introduce the word that you want to count vowels: ")
counter = 0
for i in word:
    if i in vowels:
        counter += 1

print(f"The word {word} has {counter} vowels")
