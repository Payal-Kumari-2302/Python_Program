# Program_57

# W.A.P to accept three angles of triangle and check if triangle is possible or not

a1 = int(input("Enter 1st Angle:-> "))
a2 = int(input("Enter 2nd Angle:-> "))
a3 = int(input("Enter 3rd Angle:-> "))

total = a1 + a2 + a3

if (a1 > 0 and a2 > 0 and a3 > 0 and total == 180):
    print("Triangle is Possible", total)
else:
    print("Triangle is Not Possible", total)
