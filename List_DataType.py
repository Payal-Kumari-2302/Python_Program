# Program_24
# Python List Data Type and All Important List Methods


# -----------------------------
# Creating a List
# -----------------------------

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

print("Original List:", fruits)


# -----------------------------
# Accessing List Items
# -----------------------------

print("\nAccessing Items")
print(fruits[1])          # Second item
print(fruits[-1])         # Last item
print(fruits[1:4])        # Range of index
print(fruits[:3])         # From beginning
print(fruits[2:])         # To the end
print(fruits[-4:-1])      # Negative indexing


# -----------------------------
# Changing Item Value
# -----------------------------

print("\nChanging Item Value")

fruits[2] = "mango"
print(fruits)


# -----------------------------
# Loop Through List
# -----------------------------

print("\nLoop Through List")

for x in fruits:
    print(x)


# -----------------------------
# Check Item Exists
# -----------------------------

print("\nCheck Item Exists")

if "apple" in fruits:
    print("Yes, apple is present in the list")


# -----------------------------
# Length of List
# -----------------------------

print("\nLength of List")

print(len(fruits))


# -----------------------------
# append() Method
# -----------------------------

print("\nappend() Method")

fruits.append("grapes")
print(fruits)


# -----------------------------
# extend() Method
# -----------------------------

print("\nextend() Method")

fruits.extend(["guava", "papaya"])
print(fruits)


# -----------------------------
# insert() Method
# -----------------------------

print("\ninsert() Method")

fruits.insert(1, "watermelon")
print(fruits)


# -----------------------------
# remove() Method
# -----------------------------

print("\nremove() Method")

fruits.remove("banana")
print(fruits)


# -----------------------------
# pop() Method
# -----------------------------

print("\npop() Method")

fruits.pop(2)
print(fruits)


# -----------------------------
# del Keyword
# -----------------------------

print("\ndel Keyword")

temp_list = ["a", "b", "c", "d"]

del temp_list[1]
print(temp_list)


# -----------------------------
# clear() Method
# -----------------------------

print("\nclear() Method")

temp = ["apple", "banana"]

temp.clear()
print(temp)


# -----------------------------
# copy() Method
# -----------------------------

print("\ncopy() Method")

new_list = fruits.copy()
print(new_list)


# -----------------------------
# list() Constructor
# -----------------------------

print("\nlist() Constructor")

numbers = list((1, 2, 3, 4))
print(numbers)


# -----------------------------
# count() Method
# -----------------------------

print("\ncount() Method")

names = ["Payal", "Mahi", "Payal", "Babli"]

print(names.count("Payal"))


# -----------------------------
# index() Method
# -----------------------------

print("\nindex() Method")

print(names.index("Babli"))


# -----------------------------
# sort() Method
# -----------------------------

print("\nsort() Method")

names.sort()
print(names)


# -----------------------------
# sort(reverse=True)
# -----------------------------

print("\nDescending Sort")

numbers = [5, 2, 9, 1, 7]

numbers.sort(reverse=True)
print(numbers)


# -----------------------------
# reverse() Method
# -----------------------------

print("\nreverse() Method")

numbers.reverse()
print(numbers)


# -----------------------------
# Joining Two Lists
# -----------------------------

print("\nJoining Two Lists")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print(result)


# -----------------------------
# min(), max(), sum()
# -----------------------------

print("\nmin(), max(), sum()")

values = [10, 20, 30, 40]

print("Minimum:", min(values))
print("Maximum:", max(values))
print("Sum:", sum(values))


# -----------------------------
# enumerate() Function
# -----------------------------

print("\nenumerate() Function")

students = ["Payal", "Mahi", "Babli"]

for index, value in enumerate(students):
    print(index, value)
