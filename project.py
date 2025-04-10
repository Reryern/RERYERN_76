inventory = [
    {"name": "pens", "qty": 100, "unit_price": 1000, "cost_price": 800, "product number": "A01", "brand": "nataraj"},
    {"name": "pens", "qty": 100, "unit_price": 700, "cost_price": 500, "product number": "A02", "brand": "bic"},
    {"name": "pens", "qty": 100, "unit_price": 500, "cost_price": 400, "product number": "A03", "brand": "nice"},
    {"name": "books", "qty": 100, "unit_price": 1500, "cost_price": 1200, "product number": "B01", "brand": "vista"},
    {"name": "books", "qty": 100, "unit_price": 2000, "cost_price": 1700, "product number": "B02", "brand": "araqay"},
    {"name": "books", "qty": 100, "unit_price": 1000, "cost_price": 800, "product number": "B03", "brand": "classic"},
    {"name": "pencils", "qty": 100, "unit_price": 900, "cost_price": 700, "product number": "C01", "brand": "nataraj"},
    {"name": "pencils", "qty": 100, "unit_price": 700, "cost_price": 500, "product number": "C02", "brand": "bic"},
    {"name": "pencils", "qty": 100, "unit_price": 900, "cost_price": 750, "product number": "C03", "brand": "nice"},
    {"name": "sets", "qty": 100, "unit_price": 9000, "cost_price": 8000, "product number": "D01", "brand": "oxford"},
    {"name": "sets", "qty": 100, "unit_price": 7000, "cost_price": 6000, "product number": "D02", "brand": "nataraj"},
    {"name": "sets", "qty": 100, "unit_price": 5000, "cost_price": 4000, "product number": "D03", "brand": "picfare"},
    {"name": "rubbers", "qty": 120, "unit_price": 700, "cost_price": 500, "product number": "EO1", "brand": "nataraj"},
    {"name": "rubbers", "qty": 120, "unit_price": 500, "cost_price": 300, "product number": "EO2", "brand": "bic"},
    {"name": "rubbers", "qty": 120, "unit_price": 200, "cost_price": 100, "product number": "EO3", "brand": "nice"},
]

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter the quantity: "))
    price = int(input("Enter the price: "))
    brand = input("Enter the brand: ")
    unit_price = int(input("Enter the unit price: "))
    cost_price = int(input("Enter the cost price: "))
    product_number = input("Enter the product number: ")
    item = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "brand": brand,
        "unit price": unit_price,
        "cost price": cost_price,
        "product number":product_number
    }
    inventory.append(item)
    print(item)

    return item
add_item()

