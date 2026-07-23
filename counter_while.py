# Thirty-third program: Practice while loops with two counters. First it asks
# for a number and counts up from 0 to that number; then it asks for another
# number and counts down from it to 0. Each loop updates its own counter
# variable until the condition stops being true.

# Count up: from 0 to the given number
number = int(input("Introduce the number you want to count up to: "))
i = 0
while i <= number:
    print(i)
    i += 1

# Count down: from the given number to 0
number = int(input("Introduce the number you want to count down from: "))
i = number
while i >= 0:
    print(i)
    i -= 1
