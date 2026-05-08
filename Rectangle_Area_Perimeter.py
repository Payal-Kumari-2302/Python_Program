# Program_8

# W.A.Python program to accept length and width of rectangle in cm
# and display the area and perimeter of rectangle.

l = int(input("Enter length of rectangle:-> "))
w = int(input("Enter width of rectangle:-> "))

area = l * w
perimeter = 2 * (l + w)

print("Area of rectangle:->", area)
print("Perimeter of rectangle:->", perimeter)
