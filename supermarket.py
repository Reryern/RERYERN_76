#A shop owner needs a program that can help him determine the selling price and profit margin of his items.

cost_price = int(input("Enter cost price: "))

transport_price = int(input("Enter transport price: "))

selling_price = cost_price + (0.05 * cost_price) + (0.02 * transport_price)

profit = selling_price - cost_price

if selling_price > cost_price:
    print("Profit available")
else:
    print("loss")
