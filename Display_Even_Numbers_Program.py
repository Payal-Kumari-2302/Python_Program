#Program_60

#W.A.P to accept any number and display even numbers from 1 to that number.

num = int(input("Enter any number:-> "))

for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)
