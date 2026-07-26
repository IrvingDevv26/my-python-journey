# Fortieth program: Given a list of names, ask the user for a name and search
# for it manually (without the in operator or the .index() method — the point
# is to practice manual traversal). The while loop compares position by
# position: if the name is found, show its index and stop with break; if the
# loop finishes without a break, the else runs and reports it doesn't exist.

names = ["ana", "luis", "carmen", "pedro", "sofia"]
name_search = input("Introduce the name you want to search: ").lower()
i = 0
while i < len(names):
    if name_search == names[i]:
        print(f"The name '{name_search}' is at position {i}")
        break
    i += 1
else:
    print(f"The name '{name_search}' isn't in the list")
