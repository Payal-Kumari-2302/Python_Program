#Program : Python Operators

# 1. Arithmetic Operators
a = 10
b = 5

print("Arithmetic Operators")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)
print("Exponent =", a ** b)
print("Floor Division =", a // b)

# 2. Comparison Operators
print("\nComparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# 3. Assignment Operators
print("\nAssignment Operators")
x = 10
print("Initial Value =", x)

x += 5
print("x += 5 :", x)

x -= 2
print("x -= 2 :", x)

x *= 3
print("x *= 3 :", x)

x /= 2
print("x /= 2 :", x)

# 4. Logical Operators
print("\nLogical Operators")
p = True
q = False

print("p and q =", p and q)
print("p or q =", p or q)
print("not p =", not p)

# 5. Bitwise Operators
print("\nBitwise Operators")
m = 6
n = 3

print("m & n =", m & n)
print("m | n =", m | n)
print("m ^ n =", m ^ n)
print("~m =", ~m)
print("m << 1 =", m << 1)
print("m >> 1 =", m >> 1)

# 6. Membership Operators
print("\nMembership Operators")
list1 = [1, 2, 3, 4]

print("2 in list1 =", 2 in list1)
print("5 not in list1 =", 5 not in list1)

# 7. Identity Operators
print("\nIdentity Operators")
list2 = [1, 2, 3]
list3 = list2
list4 = [1, 2, 3]

print("list2 is list3 =", list2 is list3)
print("list2 is list4 =", list2 is list4)
print("list2 is not list4 =", list2 is not list4)
