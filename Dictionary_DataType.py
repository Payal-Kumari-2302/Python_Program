# Program_27
# Python Dictionary Data Type and Dictionary Methods


# ---------------------------------
# Create and Print Dictionary
# ---------------------------------

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("Original Dictionary:", car)


# ---------------------------------
# Access Items
# ---------------------------------

print("\nAccess Dictionary Items")

print(car["model"])          # Using key
print(car.get("year"))       # Using get() method


# ---------------------------------
# Change Values
# ---------------------------------

print("\nChange Dictionary Values")

car["year"] = 2024

print(car)


# ---------------------------------
# Loop Through Dictionary
# ---------------------------------

print("\nLoop Through Dictionary Keys")

for x in car:
    print(x)


# ---------------------------------
# Print All Values
# ---------------------------------

print("\nPrint All Values")

for x in car:
    print(car[x])


# Using values() Method
print("\nvalues() Method")

for x in car.values():
    print(x)


# ---------------------------------
# Print Keys
# ---------------------------------

print("\nkeys() Method")

for x in car.keys():
    print(x)


# ---------------------------------
# items() Method
# ---------------------------------

print("\nitems() Method")

for key, value in car.items():
    print(key, ":", value)


# ---------------------------------
# Check if Key Exists
# ---------------------------------

print("\nCheck if Key Exists")

if "model" in car:
    print("Yes, 'model' is one of the keys in the dictionary")


# ---------------------------------
# Dictionary Length
# ---------------------------------

print("\nDictionary Length")

print(len(car))


# ---------------------------------
# Add Items
# ---------------------------------

print("\nAdd Items")

car["color"] = "Red"

print(car)


# ---------------------------------
# update() Method
# ---------------------------------

print("\nupdate() Method")

car.update({"price": 5000000})

print(car)


# ---------------------------------
# pop() Method
# ---------------------------------

print("\npop() Method")

car.pop("model")

print(car)


# ---------------------------------
# popitem() Method
# ---------------------------------

print("\npopitem() Method")

car.popitem()

print(car)


# ---------------------------------
# del Keyword
# ---------------------------------

print("\ndel Keyword")

student = {
    "name": "Payal",
    "age": 22
}

del student["age"]

print(student)


# ---------------------------------
# clear() Method
# ---------------------------------

print("\nclear() Method")

temp = {
    "a": 1,
    "b": 2
}

temp.clear()

print(temp)


# ---------------------------------
# copy() Method
# ---------------------------------

print("\ncopy() Method")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

mydict = car.copy()

print(mydict)


# ---------------------------------
# dict() Constructor
# ---------------------------------

print("\ndict() Constructor")

new_dict = dict(name="Payal", age=22, city="Dhanbad")

print(new_dict)


# ---------------------------------
# fromkeys() Method
# ---------------------------------

print("\nfromkeys() Method")

keys = ("name", "age", "city")

value = "Not Available"

x = dict.fromkeys(keys, value)

print(x)


# ---------------------------------
# setdefault() Method
# ---------------------------------

print("\nsetdefault() Method")

car = {
    "brand": "Ford",
    "model": "Mustang"
}

car.setdefault("color", "Black")

print(car)


# ---------------------------------
# Nested Dictionary
# ---------------------------------

print("\nNested Dictionary")

students = {
    "student1": {
        "name": "Payal",
        "age": 22
    },

    "student2": {
        "name": "Mahi",
        "age": 21
    }
}

print(students)


# ---------------------------------
# enumerate() Function
# ---------------------------------

print("\nenumerate() Function")

names = ["Payal", "Mahi", "Babli"]

for index, value in enumerate(names):
    print(index, value)
