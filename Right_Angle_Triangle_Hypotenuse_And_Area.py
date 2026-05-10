#Program_20

# W.A.Python program to accept perpendicular and base of a right angle triangle and find hypotenuse and area.

import math

p = int(input("Enter perpendicular of right angle triangle:-> "))
b = int(input("Enter base of right angle triangle:-> "))

h = math.sqrt((p * p) + (b * b))

area = (p * b) / 2

print("Hypotenuse of right angle triangle:->", h)
print("Area of right angle triangle:->", area)
