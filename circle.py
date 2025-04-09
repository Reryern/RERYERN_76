#A programto compute the diameter, circumference, and area of the circle given its radius

radius = int(input("Enter the radius of the circle: "))

diameter = 2 * radius

circumference = 2 * 3.142 * radius

area = 3.142 * radius ** 2

print(f"The diameter of the circle is {diameter}, its circumference is {circumference}, and its area is {area}")