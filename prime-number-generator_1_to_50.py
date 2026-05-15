#Program_50

# Create a loop that prints all prime numbers between 1 and 50

for num in range(2, 51):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
