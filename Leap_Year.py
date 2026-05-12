#Program_34

# W.A.Python Program to accept any year and display whether it is a leap year or not.

year=int(input("Enter any year:->"))

if((year%400==0) or (year%4==0 and year%100!=0)):
    print("Leap Year")

else:
    print("Not a Leap Year")
