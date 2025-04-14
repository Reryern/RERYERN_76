cart = [
    {"product": "apple", "type": "fruit", "price": 100, "qty": 3},
    {"product": "brocolli", "type": "vegetable", "price": 200, "qty": 5},
    {"product": "mango", "type": "fruit", "price": 250, "qty": 5},
]


def add_item():
    while True:
        product = input("Enter the product name or 'q' to stop: ").strip().lower()
        if product == "q":
            print("Exiting the program.")
            break

        # Check if the product already exists in the cart
        for existing_item in cart:
            if existing_item["product"] == product:
                print(f"Item '{product}' already exists in the cart.")
                response = input("Do you want to add more quantity? (yes/no): ").strip().lower()
                if response == "yes":
                    try:
                        additional_qty = int(input("Enter the quantity to add: ").strip())
                        if additional_qty > 0:
                            existing_item["qty"] += additional_qty
                            print(f"Updated quantity of '{product}' to {existing_item['qty']}.")
                        else:
                            print("Quantity must be greater than zero.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number for quantity.")
                else:
                    print("No additional quantity added.")
                break
        else:
            # If the product does not exist, collect details and add it as a new item
            product_type = input("Enter the product type: ").strip().lower()
            try:
                price = float(input("Enter the product price: ").strip())
                qty = int(input("Enter the product quantity: ").strip())
                if qty <= 0:
                    print("Quantity must be greater than zero.")
                    continue
            except ValueError:
                print("Invalid input for price or quantity. Please enter numeric values.")
                continue

            # Create the new item and add it to the cart
            item = {
                "product": product,
                "type": product_type,
                "price": price,
                "qty": qty
            }
            cart.append(item)
            print(f"Item '{product}' added to the cart.")

        # Display the current cart
        print("Current cart:", cart)

        # Ask if the user wants to add another item
        add_more = input("Do you want to add another item? (yes/no): ").strip().lower()
        if add_more != "yes":
            print("Exiting the program.")
            break

add_item()















