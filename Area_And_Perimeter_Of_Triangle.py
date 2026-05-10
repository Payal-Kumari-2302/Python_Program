# Program_11

# W.A.Python program to accept three sides of a triangle and calculate the area, perimeter and semi perimeter of the triangle.

import math

s1 = int(input("Enter 1st side of triangle:-> "))
s2 = int(input("Enter 2nd side of triangle:-> "))
s3 = int(input("Enter 3rd side of triangle:-> "))

# Semi-perimeter
s = (s1 + s2 + s3) / 2

# Heron's Formula
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

perimeter = s1 + s2 + s3

print("Area of triangle:->", area)
print("Perimeter of triangle:->", perimeter)
