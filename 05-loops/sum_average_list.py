# Thirty-first program: Given a list of numbers, compute and print the total
# sum and the average of its elements. The sum is accumulated in a loop and
# the average is the total divided by how many elements the list has.

numbers = [12, 45, 7, 89, 34, 23, 56]
total = 0
for number in numbers:
    total += number

average = total / len(numbers)
print(f"The total sum is: {total} and the average is: {average}")
