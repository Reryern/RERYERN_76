numbers = []

total = 0
for number in numbers:
    
    while True:
        number = int(input("Enter the number or q to exit: "))
        if number.lower() == "q":
            break
        
        numbers.append(number)
        print(numbers)





