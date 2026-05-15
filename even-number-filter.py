#Program_48

# Given a list of integers, find all the even numbers and store them in a new list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print("Even Numbers:", even_numbers)
