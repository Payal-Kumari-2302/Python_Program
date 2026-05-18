#Program_63

#W.A.P to accept two numbers and display even numbers from 1st number to 2nd number

num1 = int(input("Enter 1st number:-> "))
num2 = int(input("Enter 2nd number:-> "))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)
