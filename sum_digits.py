# Thirty-ninth program: Ask the user for a positive integer and compute the
# sum of its digits using a while loop (without converting it to a string).
# For example, for 4729 the result is 4+7+2+9 = 22. On each iteration, % 10
# extracts the last digit and //= 10 removes it, so the loop ends when the
# number runs out of digits (it becomes 0). Also display how many digits the
# number has: each iteration processes exactly one digit, so a counter inside
# the loop keeps track of them.

number = int(input("Introduce the number: "))
total_sum = 0
count_digits = 0
while number > 0:
    digit = number % 10
    total_sum += digit
    number //= 10
    count_digits += 1

print("Total sum:", total_sum)
print("Total digits:", count_digits)
