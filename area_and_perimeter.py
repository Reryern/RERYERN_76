#A program to compute the area and perimeter of a rectangle given its length and width

length = int(input("Enter the length of the rectangle: "))

width = int(input("Enter the width of the rectangle: "))

area = length * width

perimeter = 2 * (length + width)    

print(f"The area of the rectangle is {area} and its perimeter is {perimeter}")  