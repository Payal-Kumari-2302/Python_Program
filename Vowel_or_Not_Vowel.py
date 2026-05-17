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



#W.A.P to accept any character and check vowel,semi vowel or not vowel


ch=input("Enter any Character:->")
if(ch=="A" or ch=="a" or ch=="E" or ch=="e" or ch=="I" or ch=="i" or ch=="O" or ch=="o" or ch=="U" or ch=="u"):
    print("Vowel")
elif (ch=="W" or ch == "w" or ch== "Y" or ch=="y"):
    print("Semi vowel")
elif (ch=="B" or ch=="b" or ch=="C" or ch=="c" or ch== "D" or ch=="d" or ch=="F" or ch=="f" or ch=="G" or ch=="g" or ch=="H" or ch=="h" or ch=="I" or ch=="i" or ch=="J" or ch=="j" or ch=="K" or ch=="k" or ch=="L" or ch=="l" or ch=="M" or ch=="m" or ch=="N" or ch=="O" or ch=="P" or ch=="p" or ch=="Q" or ch=="R" or ch=="r" or ch=="S" or ch=="s" or ch=="T" or ch=="t" or ch=="V" or ch=="v" or ch=="X" or ch=="x" or ch=="Z" or ch=="z"):
    print("Not Vowel[Consonant]")
else:
    print("Not an alphabet")
