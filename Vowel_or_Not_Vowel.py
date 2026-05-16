#Program_55

# W.A.P to accept any character and check it vowel or not vowel

ch = input("Enter any character: ")

if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print("Vowel")
else:
    print("Not a vowel")


#Method 2: Using if-elif

ch = input("Enter any character: ").lower()

if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
else:
    print("Not a vowel")


#Method 3: Using string find

ch = input("Enter any character: ").lower()

vowels = "aeiou"

if vowels.find(ch) != -1:
    print("Vowel")
else:
    print("Not a vowel")


#Method 4: Using set (best & fast)

ch = input("Enter any character: ").lower()

vowels = {'a', 'e', 'i', 'o', 'u'}

if ch in vowels:
    print("Vowel")
else:
    print("Not a vowel")



#Method_5: Using match-case

ch = input("Enter any character: ").lower()

match ch:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("Vowel")
    case _:
        print("Not a vowel")
