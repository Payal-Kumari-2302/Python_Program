# Program_14

# W.A.Python program to accept basic salary and calculate TA, DA, HRA, Gross Salary, PF, and Net Salary.

bs = int(input("Enter Basic Salary:-> "))

ta = (bs * 10) / 100
da = (bs * 20) / 100
hra = (bs * 25) / 100
gs = bs + ta + da + hra
pf = (gs * 20) / 100
ns = gs - pf

print("Basic Salary:->", bs)
print("TA Salary:->", ta)
print("DA Salary:->", da)
print("HRA Salary:->", hra)
print("Gross Salary:->", gs)
print("PF Salary:->", pf)
print("Net Salary:->", ns)
