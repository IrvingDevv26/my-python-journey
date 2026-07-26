# Thirty-sixth program: Ask the user for an upper limit and loop through the
# numbers from 1 to that limit. Use continue to skip all multiples of 3 and
# print the ones that pass the filter. At the end, show how many numbers were
# printed and how many were skipped.

number_end = int(input("Enter the upper limit to count to: "))
count_printed = 0
count_skip = 0

i = 0
while i < number_end:
    i += 1
    if i % 3 == 0:
        count_skip += 1
        continue
    print(i)
    count_printed += 1
print(f"Numbers printed: {count_printed} | Numbers skipped: {count_skip}")
