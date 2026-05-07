#Program_4

#W.A.P to accept two number 60 and 30 and display this add,sub,mul and div using float data type.

# Method 1 Direct

a, b = 60, 30
c = a + b
d = a - b
e = a * b
f = a / b      # For floor division use: a // b
g = a % b
print("Addition =", c)
print("Subtraction =", d)
print("Multiplication =", e)
print("Division =", f)
print("Remainder=", g)


# Method 2
'''
a, b = 60, 30

print(a + b)
print(a - b)
print(a * b)
print(a / b)     # or print(a // b)
print(a % b)
'''


# Method 3 : Using User Input

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)    # or a // b
print("Remainder=", a % b )
