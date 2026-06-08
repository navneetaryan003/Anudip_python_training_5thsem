#count special characters in a given sentence.

sentence = input("Enter a sentence: ")  


count = 0   #variable to store the count of special characters

for char in sentence:
    if not char.isalnum():
        count+=1

print("The number of special characters in the given sentence is:", count)

