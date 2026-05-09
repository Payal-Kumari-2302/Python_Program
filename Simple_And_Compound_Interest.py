# Program_11

# W.A.Python program to accept principal amount,rate of interest and time in year, then calculatemSimple Interest and Compound Interest.

import math

p = int(input("Enter Principal Amount:-> "))
r = int(input("Enter Rate in %:-> "))
t = int(input("Enter Time in years:-> "))

si = (p * r * t) / 100

ci = p * math.pow((1 + r / 100), t) - p

print("Simple Interest:->", si)
print("Compound Interest:->", ci)
