#program to ask a user to enter the quantity taken and the price
name = input("What is your name? ")

print(f"Hello {name}")

item_taken = input("what item have you taken: ")

price = input("How much is the item you have taken: ")

quantity = input("How many items have you taken: ")

amount = int(price) * int(quantity)

print(f"Hey, {name} you have taken {item_taken} at a price of shs.{price} and your total amount is shs.{amount}.\nHave a nice day.")