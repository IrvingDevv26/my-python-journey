# Forty-ninth program: Print a list as a numbered to-do list starting at 1,
# formatted like "1. Comprar pan". enumerate gives both the index and the item
# on each iteration; start=1 makes the numbering begin at 1 instead of 0.

tasks = ["Comprar pan", "Llamar a mamá", "Estudiar Python", "Hacer ejercicio"]

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
