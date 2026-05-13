#Program_39

#W.A.Python program to convert kilometer into miles

km = int(input("Enter distance in kilometer:->"))

# Conversion factor: 1 km = 0.621371 miles
conversion_factor = 0.621371

miles = km * conversion_factor

print(f"{km} kilometer is equal to {miles} miles")
