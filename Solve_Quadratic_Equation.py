#Program_22

# W.A.Python program to solve quadratic equation. The standard form of quadratic equation is: ax² + bx + c = 0where a, b and c are real numbers and a ≠ 0


import math

# Input coefficients
a = float(input("Enter coefficient a:-> "))
b = float(input("Enter coefficient b:-> "))
c = float(input("Enter coefficient c:-> "))

# Calculate discriminant
discriminant = b**2 - 4*a*c

# Check condition of discriminant
if discriminant > 0:

    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    print("Root 1:->", root1)
    print("Root 2:->", root2)

elif discriminant == 0:

    # One real and repeated root
    root = -b / (2 * a)

    print("Root:->", root)

else:

    # Complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)

    print(f"Root 1:-> {real_part} + {imaginary_part}i")
    print(f"Root 2:-> {real_part} - {imaginary_part}i")
