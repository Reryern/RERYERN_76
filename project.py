inventory = []

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter the quantity: "))
    price = int(input("Enter the price: "))
    brand = input("Enterthe brand: ")
    item = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "brand": brand
    }
    inventory.append(item)
    print(inventory)

    return item
add_item()