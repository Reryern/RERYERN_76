inventory = [
    {"name": "pens", "qty": 100, "unit_price": 1000, "cost_price": 800, "product number": "A01", "brand": "nataraj"},
    {"name": "books", "qty": 100, "unit_price": 1500, "cost_price": 1200, "product number": "A02", "brand": "vista"},
    {"name": "pencils", "qty": 100, "unit_price": 900, "cost_price": 700, "product number": "A03", "brand": "nataraj"},
    {"name": "sets", "qty": 100, "unit_price": 9000, "cost_price": 8000, "product number": "A04", "brand": "oxford"},
    {"name": "rubbers", "qty": 120, "unit_price": 700, "cost_price": 500, "product number": "A05", "brand": "nataraj"},
]

def add_item():
    item_name = input("Enter name of the item you want to add: ")
    existing_item = inventory["name"]
    quantity = int(input("Enter quantity to add: "))
    for item in inventory:
        existing_quantity = inventory["qty"]
        if item_name == existing_item:
            if quantity < 0:
                print("Quantity cannot be less than or.")
                return
            else:
                existing_quantity += inventory["qty"]
                unit_price = int(input("Enter the unit price: "))
                cost_price = int(input("Enter the cost price: "))
                if unit_price > cost_price:
                    print("Cost price cannot be higher than unit price, you will incur losses.")
                else:
                    product_number = input("Enter the product number: ").capitalize()
                    brand = input("Enter the brand: ")
                    item = {
                    "name": item_name,
                    "quantity": quantity,
                    "brand": brand,
                    "unit price": unit_price,
                    "cost price": cost_price,
                    "product number":product_number
                }
        
            
                inventory.append(item)
                print(f"The added item is{item}")
                print(inventory)
        else:
        return item
add_item()




        


    
    