# Program_23

# W.A.Python program to swap two variables.


# -------------------------------
# Swap Without Using 3rd Variable
# -------------------------------

# Input two variables
a = int(input("Enter the value of 1st variable:-> "))
b = int(input("Enter the value of 2nd variable:-> "))

# Display original values
print(f"\nOriginal value: a = {a}, b = {b}")

# Swap without using third variable
a, b = b, a

# Display swapped values
print(f"Swap value: a = {a}, b = {b}")


# ----------------------------
# Swap Using 3rd Variable
# ----------------------------

# Input two variables
a = int(input("\nEnter the value of 1st variable:-> "))
b = int(input("Enter the value of 2nd variable:-> "))

# Display original values
print(f"\nOriginal value: a = {a}, b = {b}")

# Swap using third variable
temp = a
a = b
b = temp

# Display swapped values
print(f"Swap value: a = {a}, b = {b}")
