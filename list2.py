customers = []

items = []


for number in range(2):
    customers.append(input("\tEnter your name: "))
    total_amount = 0
    
    for number in range(2):
        amount = 0
        items.append(input("Enter the item taken: "))
        price = int(input("Enter the price of the item taken: "))
        
        amount += price
        total_amount += amount
       
    print(f"Your total amount is {total_amount}\n")
   



