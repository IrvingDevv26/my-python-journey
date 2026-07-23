# Thirty-fifth program: Repeatedly ask the user for numbers and accumulate
# their sum. The program stops when the user enters 0 (the "sentinel" value:
# a special input that means "stop asking"). At the end, display the total
# sum and how many numbers were entered (not counting the 0).

count_numbers = 0
total_sum = 0
while True:
    number = int(input("Please introduce a number (type 0 to end the program): "))
    if number == 0:
        break
    total_sum += number
    count_numbers += 1

print("Total sum:", total_sum)
print("Numbers entered:", count_numbers)
