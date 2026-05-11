# Program_26
# Python Set Data Type with All Important Set Methods


# ---------------------------------
# Create a Set
# ---------------------------------

fruits = {"apple", "banana", "cherry"}

print("Original Set:", fruits)


# ---------------------------------
# Access Set Items
# ---------------------------------

print("\nAccess Set Items")

for item in fruits:
    print(item)


# ---------------------------------
# Check Item Exists
# ---------------------------------

print("\nCheck Item Exists")

if "apple" in fruits:
    print("Yes, apple is present in the set")


# ---------------------------------
# Add Items
# ---------------------------------

print("\nadd() Method")

fruits.add("orange")

print(fruits)


# ---------------------------------
# update() Method
# ---------------------------------

print("\nupdate() Method")

fruits.update(["grapes", "mango", "guava"])

print(fruits)


# ---------------------------------
# Length of Set
# ---------------------------------

print("\nLength of Set")

print(len(fruits))


# ---------------------------------
# remove() Method
# ---------------------------------

print("\nremove() Method")

fruits.remove("banana")

print(fruits)


# ---------------------------------
# discard() Method
# ---------------------------------

print("\ndiscard() Method")

fruits.discard("apple")

print(fruits)


# ---------------------------------
# pop() Method
# ---------------------------------

print("\npop() Method")

numbers = {1, 2, 3, 4}

numbers.pop()     # Removes random item

print(numbers)


# ---------------------------------
# clear() Method
# ---------------------------------

print("\nclear() Method")

temp_set = {"a", "b", "c"}

temp_set.clear()

print(temp_set)


# ---------------------------------
# copy() Method
# ---------------------------------

print("\ncopy() Method")

set1 = {1, 2, 3}

new_set = set1.copy()

print(new_set)


# ---------------------------------
# union() Method
# ---------------------------------

print("\nunion() Method")

set1 = {1, 2, 3}
set2 = {4, 5, 6}

result = set1.union(set2)

print(result)


# ---------------------------------
# intersection() Method
# ---------------------------------

print("\nintersection() Method")

set1 = {1, 2, 3}
set2 = {2, 3, 4}

result = set1.intersection(set2)

print(result)


# ---------------------------------
# intersection_update() Method
# ---------------------------------

print("\nintersection_update() Method")

set1 = {1, 2, 3}
set2 = {2, 3, 4}

set1.intersection_update(set2)

print(set1)


# ---------------------------------
# difference() Method
# ---------------------------------

print("\ndifference() Method")

set1 = {1, 2, 3}
set2 = {2, 4, 5}

result = set1.difference(set2)

print(result)


# ---------------------------------
# difference_update() Method
# ---------------------------------

print("\ndifference_update() Method")

set1 = {1, 2, 3}
set2 = {2, 4, 5}

set1.difference_update(set2)

print(set1)


# ---------------------------------
# symmetric_difference() Method
# ---------------------------------

print("\nsymmetric_difference() Method")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.symmetric_difference(set2))


# ---------------------------------
# symmetric_difference_update()
# ---------------------------------

print("\nsymmetric_difference_update() Method")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.symmetric_difference_update(set2)

print(set1)


# ---------------------------------
# issubset() Method
# ---------------------------------

print("\nissubset() Method")

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))


# ---------------------------------
# issuperset() Method
# ---------------------------------

print("\nissuperset() Method")

set1 = {1, 2, 3, 4}
set2 = {1, 2}

print(set1.issuperset(set2))


# ---------------------------------
# isdisjoint() Method
# ---------------------------------

print("\nisdisjoint() Method")

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))


# ---------------------------------
# Join Two Sets
# ---------------------------------

print("\nJoin Two Sets")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

print(set3)


# ---------------------------------
# del Keyword
# ---------------------------------

print("\ndel Keyword")

temp = {"apple", "banana"}

del temp

# print(temp)
# This will raise an error because set no longer exists


# ---------------------------------
# Empty Set
# ---------------------------------

print("\nEmpty Set")

empty_set = set()

print(empty_set)


# ---------------------------------
# Set Constructor
# ---------------------------------

print("\nSet Constructor")

numbers = set((1, 2, 3, 4))

print(numbers)


# ---------------------------------
# min(), max(), sum()
# ---------------------------------

print("\nmin(), max(), sum()")

values = {10, 20, 30, 40}

print("Minimum:", min(values))
print("Maximum:", max(values))
print("Sum:", sum(values))


# ---------------------------------
# enumerate() Function
# ---------------------------------

print("\nenumerate() Function")

names = {"Payal", "Mahi", "Babli"}

for index, value in enumerate(names):
    print(index, value)
