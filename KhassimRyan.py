Name = input("What is your name? ")

print(f"Hello, {Name}")

item_taken = input("Which item have you taken? ")

quantity_taken = input("How much have you taken? ")

price = input("what is the price on the label? ")

total_amount = int(quantity_taken) * int(price)

Address = input("Where do you live? ")

print(f"Hey, {Name} you have taken {item_taken} at price of shs.{price}, your total is shs.{total_amount} and you live in {Address}.\nHave a nice day and thank you for coming.")