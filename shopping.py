# A restaurant wants a simple system to manage customr orders zand generate bills

print('''print..........Item Menu.............
      1. Burger\t\t 25000
      2. Pizza\t\t 40000
      3. Soda\t\t 5000
      4. Coffee\t\t 8000''')

item_code = int(input("Enter item code: "))

item_quantity = int(input("Enter quantity: "))

item_price = 0

discount = 0

if item_code == 1:
    print("Burger")
    if item_quantity >= 2:
        item_price = 25000 * item_quantity
        discount = 0.1 * (25000 * item_quantity)
        cost = item_price - discount 
        print(cost)
    else:
        item_price = 25000 * item_quantity
        print("No discount")    
elif item_code == 2:
    print("Pizza")  
    item_price = 40000 * item_quantity      
elif item_code == 3:
    print("Soda")
    item_price = 5000 * item_quantity 
elif item_code == 4:
    print("Coffee")
    item_price = 8000 * item_quantity
else:
    print("Invalid option")
print(item_price)
