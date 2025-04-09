#A program to ask a user to enter amount in USD and convert it to Ugshs

amount = int(input("Enter the amount in USD: "))

exchange_rate = 3600

amount_in_ugshs = amount * exchange_rate

print(f"The amount in Ugshs is {amount_in_ugshs}")
