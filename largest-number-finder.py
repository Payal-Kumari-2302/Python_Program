#Program_47

# Implement a program that finds the largest number in a list

# Method_1

numbers = [2, 4, 6, 10, 100]

greatest = max(numbers)

print("Largest number is:", greatest)

#Method_2

# Find the largest number in a list without using max()

numbers = [2, 4, 6, 10, 100]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
