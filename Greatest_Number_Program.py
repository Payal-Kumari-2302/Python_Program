#Program_36

# W.A.Python program to accept any two number and display the greatest number or both are same.

n1=int(input("Enter 1st Number:->"))
n2=int(input("Enter 2nd Number:->"))

if n1>n2:
    print("Greatest Number is:->",n1)

elif n2>n1:
    print("Greatest Number is:->",n2)

else:
    print("Both numbers are same")
