#Program_54


# Given a list of names, print all names starting with the letter 'A'

names = ["Payal", "Amisha", "mahi", "Awantika", "Priyanshi", "Ankit", "Ajay"]

# Method 1: Using startswith()

print("Method 1:")
for i in names:
    if i.startswith('A'):
        print(i)



# Method 2: Using index [0]

print("\nMethod 2:")
for i in names:
    if i[0] == 'A':
        print(i)
