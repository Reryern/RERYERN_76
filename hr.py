#A program asking the user to enter the employee name, hours worked, the program should display above average if hours worked are above 50. The program should compute the basic wage at a rate of 30000 if the hours worked are 50 and above otherwise the rate is 25000.

Name = input("What is your name? : ")

AVERAGE_HOURS= 50
ABOVE_AVERAGE_RATE = 30000
BELOW_AVERAGE_RATE = 25000

hours_worked = int(input("How many hours have you worked? : "))

if hours_worked >= AVERAGE_HOURS:
    print(f"You are above average.")
    wage = hours_worked * ABOVE_AVERAGE_RATE

else:
    print(f"You are below average.")
    wage = hours_worked * BELOW_AVERAGE_RATE

print(f"Your salary is {wage}")    