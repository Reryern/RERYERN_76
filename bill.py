#printing amount given the price and quantity 
price = 1500
quantity = 5 
discount = 0.05
amount = price * quantity
net_amount = amount - discount * amount
print(f" The amount is {amount}\n The discount is {discount * amount}\n The net_amount is {net_amount}")