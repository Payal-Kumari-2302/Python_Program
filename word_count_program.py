#Program_44

#Program_49

# Python Program to Count the Number of Words in a Sentence Using Different Methods


# Method_1 : Using split() and len()

sentence = input("Enter a sentence:-> ")

words = sentence.split()

count = len(words)

print("Number of words:", count)



# Method_2 : Using count() Method

sentence = input("Enter a sentence:-> ")

word_count = sentence.count(" ") + 1

print("Number of words:", word_count)



# Method_3 : Using Predefined Sentence

sentence = "Python is a very popular language in the world"

words = sentence.split()

count = len(words)

print("Number of words:", count)
