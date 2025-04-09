currencies = {"YEN": 2750, "GBP": 3750, "USD": 4750, "CHF": 5750, "JPY": 6750}

amount = int(input("Enter the currency in UGX: "))
currency = input("Enter the currency you want to convert to: ")

new_amount = amount/currencies.get(currency)
print(new_amount)

