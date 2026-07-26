# Thirty-eighth program: Given a list of numbers, loop through it and count
# how many numbers are positive, how many are negative, and how many are
# zero, while also accumulating the total sum. Display all three counters
# plus the total sum at the end.

numbers = [12, -5, 0, 34, -8, 7, 0, -3, 21]
i = 0
counter_positive = 0
counter_negative = 0
counter_zero = 0
total_sum = 0
while i < len(numbers):
    if numbers[i] > 0:
        counter_positive += 1
    elif numbers[i] < 0:
        counter_negative += 1
    else:
        counter_zero += 1
    total_sum += numbers[i]
    i += 1

print("Positive:", counter_positive)
print("Negative:", counter_negative)
print("Zero:", counter_zero)
print("Total sum:", total_sum)
