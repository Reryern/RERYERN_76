# A program that computes weekly payroll for its salespeople

employee_name = input("Enter employee name: ")
employee_number = input("Enter employee number: ")
weekly_total_sales = int(input("Enter weekly total sales: "))

base_pay = 1000000

commission1 = 0.1 * 5000000
commission2 = 0.15 * (weekly_total_sales - 5000000)

if weekly_total_sales <=5000000:
    commission1 = 0.1 * 5000000
    salary = commission1 + base_pay
    print(f"Your salary is {salary}")
elif weekly_total_sales > 5000000:
    commission1 = 0.1 * 5000000
    commission2 = 0.15 * (weekly_total_sales - 5000000)
    salary = base_pay + commission1 + commission2
    print(f"Your salary is {salary}")
else:
    print("No commission for you.")
    print(f"Your salary is {weekly_total_sales}")