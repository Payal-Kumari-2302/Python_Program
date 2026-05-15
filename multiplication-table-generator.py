#Program_49

# Implement a program that prints the multiplication table of a given number

#Method_1 For loop

num = int(input("Enter any number:-> "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)



#Method_2 while loop 

# Multiplication table using while loop

num = int(input("Enter any number:-> "))

i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1



Method 3: f-string use karke (clean output)

num = int(input("Enter any number:-> "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


