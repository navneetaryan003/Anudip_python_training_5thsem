#write a program to input a sentence from the user and count the frequency of vowels in a given sentence.

sentence = input("Enter a sentence: ")

#vowels
vowels = "aeiouAEIOU"

#counting the frequency of vowels
frequency = {}     #dictionary to store the frequency of each vowel
for char in sentence:
    if char in vowels:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

#displaying the frequency of vowels
print("Frequency of vowels in the given sentence:")
for vowel, count in frequency.items():
    print(f"{vowel}: {count}")  
    
