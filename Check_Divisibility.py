#Program_35

# W.A.Python program to accept any number and check:
# divisible by 3,
# divisible by 5,
# divisible by both 3 and 5,
# or not divisible by both.

n=int(input("Enter Any Number:->"))

if n%3==0 and n%5!=0:
    print("Number is divisible by 3 =",n)

elif n%5==0 and n%3!=0:
    print("Number is divisible by 5 =",n)

elif n%3==0 and n%5==0:
    print("Number is divisible by both 3 and 5 =",n)

else:
    print("Number is not divisible by both 3 and 5 =",n)
