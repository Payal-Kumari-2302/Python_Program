# Program

# W.A.Python program to accept the radius of a circle
# and display area, diameter, and circumference.

radius = float(input("Enter radius of a circle:-> "))

area = (22 / 7) * radius * radius
diameter = 2 * radius
circumference = 2 * (22 / 7) * radius

print("Area of circle:->", area)
print("Diameter of circle:->", diameter)
print("Circumference of circle:->", circumference)
