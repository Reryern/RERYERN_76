# A program to ask a user how much money they want to deposit,withdraw and check balance.

print('''........Options.......
        1. Deposit
        2. Withdraw
        3. Check balance''')

Option = int(input("Please select an option: "))

MINIMUM_DEPOSIT = 5000

current_balance = 100000

if Option == 1:
    deposit_amount = int(input("Enter deposit amount: "))
    if deposit_amount <= MINIMUM_DEPOSIT:
        current_balance = current_balance + deposit_amount
        print("Minimum deposit should be 5000")
    else:
        print(f"you have deposited: {deposit_amount} and your cuurent balance is: {current_balance}")
elif Option == 2:
    withdraw = int(input("Enter the money you want to withdraw: "))   
    if current_balance > withdraw:
        pin_code = int(input("Enter PIN code: "))
        balance = current_balance - withdraw
        print(f"You have withdrawn {withdraw} and your current balance is {balance}")
    else:
        print(f"Current balance is less than withdraw amount")
elif Option == 3:
    print(current_balance)
else:
    print("Invalid Option.")