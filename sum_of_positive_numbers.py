#Program_43

# Given a list of integers, find the sum of all positive numbers

numbers = [5, -2, 10, -7, 8]

sum_positive = 0

if numbers[0] > 0:
    sum_positive += numbers[0]

if numbers[1] > 0:
    sum_positive += numbers[1]

if numbers[2] > 0:
    sum_positive += numbers[2]

if numbers[3] > 0:
    sum_positive += numbers[3]

if numbers[4] > 0:
    sum_positive += numbers[4]

print("Sum of positive numbers is:", sum_positive)
