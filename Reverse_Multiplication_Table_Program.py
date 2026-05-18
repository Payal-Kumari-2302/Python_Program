#Program_60

#W.A.P to accept any number and display its table in reverse order

num = int(input("Enter any number:-> "))

print("Table in reverse order")

for i in range(10, 0, -1):
    print(num, "x", i, "=", num * i)
