#Program_40

# W.A.Python program to display calendar

import calendar

year = int(input("Enter any year:->"))
month = int(input("Enter any month:-> "))

cal = calendar.month(year, month)

print(cal)
