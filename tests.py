values = []

no_of_values = 5

for number in range(no_of_values):
    average = sum(values)/no_of_values
    digit = int(input("Enter the value: "))
    values.append(digit)
    maximum = max(values)
    minimum = min(values)
print(f"The maximum value is {maximum}, the minimum value is {minimum}, the average is {average}")

ascending_sorted = sorted(values)
descending_sorted = sorted(values, reverse=True)
print(ascending_sorted)
print(descending_sorted)

for number in range(no_of_values):
    if digit % 2 == 0:
        print("Even")
    else:
        print("Odd")