#count the character in the sentence without using len function

sentence = input("Enter a sentence: ")

count = 0
for char in sentence:
    count += 1

print("The number of characters in the given sentence is:", count)

