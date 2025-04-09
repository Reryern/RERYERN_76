#n a certain supermarket, a customer can pick upto 5 items.Write a program to capture the item taken,quantity and price and the total bill of all items. The program computes the amount of each item and then the total bill.

total_amount = 0
discount = 0
while True:
    item_taken = input(" please enter the item or S to stop: ")

    if item_taken == "S":
        break
    quantity = int(input(" eneter the quantity: "))
    price = int(input(" enter item price: "))

    amount = quantity * price
    
    print(f"\nThe total amount for {item_taken} is {amount}")

    total_amount = amount + total_amount

    
if total_amount >= 50000:
    discount = 0.1 * total_amount
    print(f"You have been given a discount of {discount}")
        
print(f"\nThe total bill is {total_amount - discount}")
  


