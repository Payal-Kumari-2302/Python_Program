# Program_29

# W.A.Python program to accept any number and display whether it is even or odd.


num = int(input("Enter any number:-> "))

if num % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")


#Method_2
#Using Ternary Operator

num = int(input("Enter any number:-> "))

print("Even Number" if num % 2 == 0 else "Odd Number")


#Method_3
#Using Bitwise Operator

num = int(input("Enter any number:-> "))

if num & 1:
    print("Odd Number")
else:
    print("Even Number")


#method_4
#Using Function

def check(num):

    if num % 2 == 0:
        return "Even Number"

    return "Odd Number"


num = int(input("Enter any number:-> "))

print(check(num))
