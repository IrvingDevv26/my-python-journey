# Twenty-sixth program: Ask the user for an upper limit and print all the even
# numbers first, then all the odd numbers, within the range from 1 to that
# limit. Even numbers use a step of 2 starting at 2, odd numbers start at 1.

range_introduced = int(input("Introduce the number you want to end to print: "))


print("-----Even numbers-----")
for i in range(2, range_introduced + 1, 2):
    print(i)

print("-----Odd numbers-----")
for i in range(1, range_introduced + 1, 2):
    print(i)
