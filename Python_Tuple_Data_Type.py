# Program_25
# Python Tuple Data Type with All Tuple Operations and Methods


# ---------------------------------
# Create a Tuple
# ---------------------------------

fruits = ("apple", "banana", "cherry")

print("Original Tuple:", fruits)


# ---------------------------------
# Access Tuple Items
# ---------------------------------

print("\nAccess Tuple Items")

print("Second Item:", fruits[1])
print("Last Item:", fruits[-1])


# ---------------------------------
# Range of Index
# ---------------------------------

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print("\nRange of Index")

print(fruits[2:5])      # Return 3rd, 4th and 5th items
print(fruits[:3])       # From beginning
print(fruits[2:])       # From index 2 to end


# ---------------------------------
# Range of Negative Index
# ---------------------------------

print("\nRange of Negative Index")

print(fruits[-4:-1])


# ---------------------------------
# Change Tuple Values
# ---------------------------------

print("\nChange Tuple Values")

# Convert tuple into list
x = ("apple", "banana", "cherry")

y = list(x)
y[1] = "kiwi"

# Convert list back into tuple
x = tuple(y)

print(x)


# ---------------------------------
# Loop Through Tuple
# ---------------------------------

print("\nLoop Through Tuple")

fruits = ("apple", "banana", "cherry")

for item in fruits:
    print(item)


# ---------------------------------
# Check if Item Exists
# ---------------------------------

print("\nCheck Item Exists")

if "apple" in fruits:
    print("Yes, apple is present in the tuple")


# ---------------------------------
# Tuple Length
# ---------------------------------

print("\nTuple Length")

print(len(fruits))


# ---------------------------------
# Tuple is Immutable
# ---------------------------------

print("\nTuple is Immutable")

fruits = ("apple", "banana", "cherry")

# fruits[1] = "orange"
# This will raise an error because tuple is immutable

print(fruits)


# ---------------------------------
# Create Tuple with One Item
# ---------------------------------

print("\nTuple with One Item")

single_tuple = ("apple",)

print(single_tuple)
print(type(single_tuple))


# Not a tuple
not_tuple = ("apple")

print(not_tuple)
print(type(not_tuple))


# ---------------------------------
# Remove Tuple
# ---------------------------------

print("\nRemove Tuple")

temp_tuple = ("apple", "banana", "cherry")

del temp_tuple

# print(temp_tuple)
# This will raise an error because tuple no longer exists


# ---------------------------------
# Empty Tuple
# ---------------------------------

print("\nEmpty Tuple")

empty_tuple = ()

print(empty_tuple)


# ---------------------------------
# Join Two Tuples
# ---------------------------------

print("\nJoin Two Tuples")

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

print(tuple3)


# ---------------------------------
# Tuple Constructor
# ---------------------------------

print("\nTuple Constructor")

fruits = tuple(("apple", "banana", "cherry"))

print(fruits)


# ---------------------------------
# count() Method
# ---------------------------------

print("\ncount() Method")

fruits = ("apple", "banana", "cherry", "apple")

x = fruits.count("apple")

print(x)


# ---------------------------------
# index() Method
# ---------------------------------

print("\nindex() Method")

fruits = ("apple", "banana", "cherry")

x = fruits.index("cherry")

print(x)


# ---------------------------------
# min(), max() and sum()
# ---------------------------------

print("\nmin(), max() and sum()")

numbers = (10, 20, 30, 40, 50)

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# ---------------------------------
# Enumerate Function
# ---------------------------------

print("\nenumerate() Function")

names = ("Payal", "Mahi", "Babli")

for index, value in enumerate(names):
    print(index, value)
