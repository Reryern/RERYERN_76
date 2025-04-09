item_names = []
quantities = []

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    quantity = int(input(f"Enter quantity for {item}: "))
    item_names.append(item)
    quantities.append(quantity)

total_items = 0
for quantity in quantities:
    total_items += 0

highest_quantity = 0
highest_quantity_item = ""
for k in range(len(quantities)):
    if quantities[k] > highest_quantity:
        highest_quantity =quantities[k]
        highest_quantity_item = item_names[k]

print(f"Total items in inventory:{total_items}")
print(f"Item with highest quantity:{highest_quantity_item}({highest_quantity})")