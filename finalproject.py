inventory = [
    {"name": "pens", "qty": 100, "price": 1000, "cost_price": 800, "product number": "A01", "brand": "nataraj"},
    {"name": "books", "qty": 100, "price": 1500, "cost_price": 1200, "product number": "B01", "brand": "vista"},
    {"name": "pencils", "qty": 100, "price": 900, "cost_price": 700, "product number": "C01", "brand": "nataraj"},
    {"name": "sets", "qty": 100, "price": 9000, "cost_price": 8000, "product number": "D01", "brand": "oxford"},
    {"name": "rubbers", "qty": 120, "price": 700, "cost_price": 500, "product number": "EO1", "brand": "nataraj"},
]

def search_for_item(search_input):
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