# Program

# W.A.Python program to find the square root, cube root, and fourth root of a given number.

import math

num = int(input("Enter any number:-> "))

square_root = math.sqrt(num)

cube_root = math.pow(num, 1/3)

fourth_root = math.pow(num, 1/4)

print("Square root of given number:->", square_root)
print("Cube root of given number:->", cube_root)
print("Fourth root of given number:->", fourth_root)
