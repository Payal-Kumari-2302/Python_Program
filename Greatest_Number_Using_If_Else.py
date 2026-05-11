# Program_28

# if, elif and else Statement
# W.A.Python program to accept any two numbers and display the greatest number.


# ---------------------------------
# Using if Statement
# ---------------------------------

num1 = int(input("Enter 1st number:-> "))
num2 = int(input("Enter 2nd number:-> "))

if num1 > num2:
    print("Greatest number:", num1)

if num2 > num1:
    print("Greatest number:", num2)

if num1 == num2:
    print("Both numbers are equal")


# ---------------------------------
# Using else Statement
# ---------------------------------

num1 = int(input("\nEnter 1st number:-> "))
num2 = int(input("Enter 2nd number:-> "))

if num1 > num2:
    print("Greatest number:", num1)
else:
    print("Greatest number:", num2)


# ---------------------------------
# Using if, elif and else Statement
# ---------------------------------

num1 = int(input("\nEnter 1st number:-> "))
num2 = int(input("Enter 2nd number:-> "))

if num1 > num2:
    print("Greatest number:", num1)

elif num2 > num1:
    print("Greatest number:", num2)

else:
    print("Both numbers are equal")
