

allowance_rate = 0.1
tax_rate = 0.05


def compute_wage(hours_worked, rate):
    #We are calculating the wage here
    wage = hours_worked * rate

    return wage

def compute_allowance(wage, allowance_rate):
    #We are calculating the allowance here
    allowance = wage *allowance_rate

    return  allowance

def compute_gross_wage(allowance, wage):
    #We are calculating the gross wage here
    gross_wage = allowance + wage

    return gross_wage

def compute_tax(gross_wage, tax_rate):
    #We are calculating the tax here
    tax_paid = tax_rate * gross_wage

    return tax_paid

def compute_net_wage(wage, allowance, tax):
    #We are calculating the net wage here
    net_wage = (wage + allowance) - tax

    return net_wage

hours_worked = int(input("Enter the hours worked: "))
rate = int(input("Enter the rate: "))



wage = compute_wage(hours_worked, rate)
allowance = compute_allowance(wage, allowance_rate)
gross_wage = compute_gross_wage(allowance, wage)
tax = compute_tax(gross_wage, tax_rate)
net_wage = compute_net_wage(wage, allowance, tax)


print(wage)
print(allowance)
print(gross_wage)
print(tax)
print(net_wage)