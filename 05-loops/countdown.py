# Twenty-seventh program: Simulate a countdown. Ask the user for a starting
# number and print every number from there down to 1, then print "Booom!" at
# the end. The range uses a step of -1 to go backwards.

number_start = int(input("Introduce what number you want to start: "))

for i in range(number_start, 0, -1):
    print(i)
print("Booom!")
