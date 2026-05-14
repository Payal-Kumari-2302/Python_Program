#Program_42

# W.A.Python program to convert days into years, weeks, and days

days = int(input("Enter number of days:-> "))

years = days // 365
remaining_days = days % 365

weeks = remaining_days // 7
days_left = remaining_days % 7

print("Years:", years)
print("Weeks:", weeks)
print("Days:", days_left)
