# A program to calculate an employee's wages.

employee_name = input("Enter employee name: ")

hours_worked = int(input("Enter hours worked: "))

extra_hours = int(input("Enter extra hours worked: "))

if hours_worked <= 40:
    salary = hours_worked * 30000
    print(salary)
else:
    extra_hours = extra_hours * 15000
    salary = (hours_worked * 30000) + extra_hours
    print(salary)

print(f"The salary for {employee_name} is {salary}")