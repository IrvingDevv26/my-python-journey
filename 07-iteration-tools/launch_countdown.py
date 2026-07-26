# Fifty-first program: Launch sequence. First print a countdown from 10 to 1
# using reversed(range(...)), then display the phases in reverse order using
# reversed on the list. reversed() gives back the elements from last to first
# without modifying the original.

phases = ["Ignición", "Motores encendidos", "Torre liberada", "Despegue"]

print("---Countdown---")
for number in reversed(range(1, 11)):
    print(number)

print("\n---Phases in reverse---")
for phase in reversed(phases):
    print(phase)
