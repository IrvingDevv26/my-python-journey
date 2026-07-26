# Thirty-second program: Find the largest value in a list and its position
# (index). It assumes the first element is the biggest, then compares it
# against the rest, updating the value and the index when a larger one appears.

numbers = [1, 8, 33, 72, 56, 90, 21]
biggest = numbers[0]
position = 0
for i in range(len(numbers)):
    if numbers[i] > biggest:
        biggest = numbers[i]
        position = i
print(f"The largest value is {biggest} at index {position}")
