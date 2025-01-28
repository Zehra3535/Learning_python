import math

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(rf"The area of the circle is: {round(area, 2)} cm^2 ")

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Hypotenuse is= {round(hypotenuse, 2)} ")
