#Program_21

# W.A.Python program to accept kilometer and convert it into millimeter, centimeter, decimeter, meter, decameter, and hectometer.

km = int(input("Enter kilometer:-> "))

mm = km * 10**6
cm = km * 10**5
dm = km * 10**4
m = km * 10**3
decam = km * 10**2
hm = km * 10

print("Millimeter:->", mm)
print("Centimeter:->", cm)
print("Decimeter:->", dm)
print("Meter:->", m)
print("Decameter:->", decam)
print("Hectometer:->", hm)
