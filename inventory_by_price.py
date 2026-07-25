# Fifty-fourth program: Given two parallel lists (products and prices), join
# them with zip and display the inventory sorted from cheapest to most
# expensive. sorted with key=lambda pair: pair[1] sorts the (product, price)
# pairs by their second element (the price). After sorting, the first pair is
# the cheapest and the last one is the most expensive.

products = ["Laptop", "Mouse", "Teclado", "Monitor", "Cable"]
prices = [1200, 25, 80, 450, 10]

inventory = sorted(zip(products, prices), key=lambda pair: pair[1])

print("---Inventory (cheapest to most expensive)---")
for product, price in inventory:
    print(f"{product}: {price}")

cheapest = inventory[0]
most_expensive = inventory[-1]
print(f"\nCheapest: {cheapest[0]} ({cheapest[1]})")
print(f"Most expensive: {most_expensive[0]} ({most_expensive[1]})")
