# Thirty-seventh program: Guessing game. The program picks a random secret
# number between 1 and 10, and the user has 5 attempts to guess it. On each
# attempt it says whether the guess is too high or too low. If the user gets
# it right, the loop exits with break; if they run out of attempts, the
# loop's else runs (it only executes when the while ends without a break)
# and reveals the secret number.

import random

number = random.randint(1, 10)
attempts = 0
while attempts < 5:
    attempts += 1
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess == number:
        print("You guessed it in attempt", attempts)
        break
    if guess > number:
        print("The number is smaller.")
    else:
        print("The number is bigger.")
else:
    print("You ran out of attempts. The number was", number)
