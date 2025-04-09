from datetime import datetime
import random

inventory = [
    {"name": "pens", "qty": 100, "price": 1000, "cost_price": 800, "product number": "A01", "brand": "nataraj"},
    {"name": "pens", "qty": 100, "price": 700, "cost_price": 500, "product number": "A02", "brand": "bic"},
    {"name": "pens", "qty": 100, "price": 500, "cost_price": 400, "product number": "A03", "brand": "nice"},
    {"name": "books", "qty": 100, "price": 1500, "cost_price": 1200, "product number": "B01", "brand": "vista"},
    {"name": "books", "qty": 100, "price": 2000, "cost_price": 1700, "product number": "B02", "brand": "araqay"},
    {"name": "books", "qty": 100, "price": 1000, "cost_price": 800, "product number": "B03", "brand": "classic"},
    {"name": "pencils", "qty": 100, "price": 900, "cost_price": 700, "product number": "C01", "brand": "nataraj"},
    {"name": "pencils", "qty": 100, "price": 700, "cost_price": 500, "product number": "C02", "brand": "bic"},
    {"name": "pencils", "qty": 100, "price": 900, "cost_price": 750, "product number": "C03", "brand": "nice"},
    {"name": "sets", "qty": 100, "price": 9000, "cost_price": 8000, "product number": "D01", "brand": "oxford"},
    {"name": "sets", "qty": 100, "price": 7000, "cost_price": 6000, "product number": "D02", "brand": "nataraj"},
    {"name": "sets", "qty": 100, "price": 5000, "cost_price": 4000, "product number": "D03", "brand": "picfare"},
    {"name": "rubbers", "qty": 120, "price": 700, "cost_price": 500, "product number": "EO1", "brand": "nataraj"},
    {"name": "rubbers", "qty": 120, "price": 500, "cost_price": 300, "product number": "EO2", "brand": "bic"},
    {"name": "rubbers", "qty": 120, "price": 200, "cost_price": 100, "product number": "EO3", "brand": "nice"},
]

def search_item(search_input=None):
    """Search for items in the inventory by dynamically matching the input."""
    results = []
    for item in inventory:
        if (
            search_input is None or
            search_input.lower() in item["name"].lower() or
            search_input.lower() in item["product number"].lower() or
            search_input.lower() in item["brand"].lower()
        ):
            results.append(item)
    return results

def generate_receipt(item, quantity, total_cost):
    """Generate and display a receipt for the purchase."""
    receipt_number = f"R-{random.randint(1000, 9999)}"
    sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n--- Receipt ---")
    print(f"Receipt Number: {receipt_number}")
    print(f"Sale Date: {sale_date}")
    print(f"Product Number: {item['product number']}")
    print(f"Item Name: {item['name']}")
    print(f"Quantity Sold: {quantity}")
    print(f"Unit Price: {item['price']}")
    print(f"Total Cost: {total_cost}")
    print("----------------\n")

def display_profit(item, quantity):
    """Display the profit made from the sale to the inventory owner."""
    profit = (item["price"] - item["cost_price"]) * quantity
    print(f"Profit made from selling {quantity} {item['name']}: {profit}")

def purchase_item():
    """Handle purchasing multiple items in one session."""
    while True:
        search_input = input("Enter search criteria (e.g., name, product number, or brand): ").strip()
        items = search_item(search_input if search_input else None)
        if items:
            try:
                print("\nItems Found:")
                for idx, item in enumerate(items, start=1):
                    print(f"{idx}. Name: {item['name']}, Quantity: {item['qty']}, Price: {item['price']}, Product Number: {item['product number']}, Brand: {item['brand']}")
                choice = int(input("Select the item number you want to purchase: "))
                if choice < 1 or choice > len(items):
                    print("Invalid choice.")
                    continue
                item = items[choice - 1]
                quantity = int(input(f"How many {item['name']} do you want?: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                elif quantity > item["qty"]:
                    print(f"Sorry, we only have {item['qty']} {item['name']} in stock.")
                else:
                    total_cost = quantity * item["price"]
                    item["qty"] -= quantity  # Update the quantity of the purchased item
                    print(f"The total cost for {item['name']} is {total_cost}.")
                    print(f"Remaining {item['name']} in stock: {item['qty']}")  # Display remaining quantity for the specific item
                    generate_receipt(item, quantity, total_cost)
                    display_profit(item, quantity)  # Display profit to the inventory owner
                    # Recalculate total items left in inventory
                    total_items_left = sum(i["qty"] for i in inventory)
                    print(f"Total items left across all inventory: {total_items_left}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Sorry, no items found matching the given criteria.")
        
        another_item = input("Do you want to purchase another item? (yes/no): ").strip().lower()
        if another_item != "yes":
            print("Thank you for your purchases!")
            break

def add_item():
    """Add a new item to the inventory."""
    item_name = input("Enter the name of the item to add: ").strip()
    try:
        item_qty = int(input("Enter the quantity of the item: "))
        item_price = int(input("Enter the price of the item: "))
        product_number = input("Enter the product number of the item: ").strip()
        date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if item_qty <= 0 or item_price <= 0:
            print("Quantity and price must be positive numbers.")
            return
        existing_item = next((item for item in inventory if item["product number"].lower() == product_number.lower()), None)
        if existing_item:
            existing_item["qty"] += item_qty
            print(f"Updated {item_name}: New quantity is {existing_item['qty']}.")
        else:
            inventory.append({
                "name": item_name,
                "qty": item_qty,
                "price": item_price,
                "product number": product_number,
                "date added": date_added
            })
            print(f"Added {item_name} to the inventory.")
    except ValueError:
        print("Invalid input. Quantity and price must be numbers.")

def display_inventory():
    """Display the current inventory."""
    if not inventory:
        print("\nThe inventory is currently empty.")
    else:
        print("\nCurrent Inventory:")
        for item in inventory:
            print(f"Name: {item['name']}, Quantity: {item['qty']}, Price: {item['price']}")
    print()

def search_and_display_item():
    """Search for items in the inventory and display their details."""
    search_input = input("Enter search criteria (e.g., name, product number, or brand): ").strip()
    items = search_item(
        search_input if search_input else None
    )
    if items:
        print(f"\nItems Found:")
        for item in items:
            print(f"Name: {item['name']}, Quantity: {item['qty']}, Price: {item['price']}, Product Number: {item['product number']}, Brand: {item['brand']}")
    else:
        print("Sorry, no items found matching the given criteria.")

def main():
    """Main function to run the inventory system."""
    while True:
        print("\nInventory Management System")
        print("1. Purchase an item")
        print("2. Add a new item")
        print("3. View inventory")
        print("4. Search for an item")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            purchase_item()
        elif choice == "2":
            add_item()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            search_and_display_item()
        elif choice == "5":
            print("Have a nice day. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()