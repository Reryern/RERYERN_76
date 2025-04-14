# A program to ask a user how much money they want to deposit,withdraw and check balance.

print('''........Bnak Account Management.......
        1. Deposit
        2. Withdraw
        3. Check balance
        4. Exit''')

option = int(input("Please select an option: "))

MINIMUM_DEPOSIT = 0

current_balance = 100000

while True:
    if option == 1:
        deposit_amount = int(input("Enter deposit amount: "))
        if deposit_amount >= MINIMUM_DEPOSIT:
            current_balance = current_balance + deposit_amount
            print(f"you have deposited: {deposit_amount} and your cuurent balance is: {current_balance}")
            break
        else:
            print(F"Minimum deposit should be {MINIMUM_DEPOSIT}")
            
    elif option == 2:
        withdraw = int(input("Enter the money you want to withdraw: "))   
        if current_balance > withdraw:
            pin_code = int(input("Enter PIN code: "))
            balance = current_balance - withdraw
            print(f"You have withdrawn {withdraw} and your current balance is {balance}")
        else:
            print(f"Current balance is less than withdraw amount")
    elif option == 3:
        print(current_balance)
    elif option == 4:
        print("Thank you for coming. Have a nice day.")
    else:
        print("Invalid option.")