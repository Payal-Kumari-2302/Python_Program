#Program_31

# W.A.Python program to accept any age and display voting eligibility.

#Method_1

age=int(input("Enter your Age:->"))

if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#Method_2

age=int(input("Enter your Age:->"))
citizen=input("Are you a citizen? (yes/no):->")

if age>=18:
    if citizen=="yes":
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("Under Age")
