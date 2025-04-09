'''Program to ask a user for the employee name, gender and hours worked. the program then computes the wage as the product of hours worked and a fixed rate of 40000. Also computes allowance as 10% of the wage, gross wage which is the summation of wage and allowance, tax is 5% of the gross wage and net wage is difference of gross wage and tax. the program should output the required details.'''

employee_name = input("What is your name?: ")

gender = input("What is your gender?: ")

hours_worked = input("How many hours have you worked?: ")

fixed_rate = 40000

wage =  int(hours_worked) * fixed_rate

allowance = 0.1 * wage

gross_wage = wage + allowance

tax = 0.05 * gross_wage

net_wage = gross_wage - tax

print(f"wage = {wage}\nallowance = {allowance}\ngross_wage = {gross_wage}\ntax = {tax}\nnet_wage = {net_wage}")