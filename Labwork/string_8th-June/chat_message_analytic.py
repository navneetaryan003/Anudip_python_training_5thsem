# Chat Message Analytics
# Problem Statement
# A chat application stores a message:
# Python is awesome and Python is easy to learn
# Tasks
# Write a program to:
# 1. Count total characters.
# 2. Count total words.
# 3. Find the longest word.
# 4. Find the shortest word.
# 5. Count how many times the word "Python" appears.
# 6. Create a list of words having more than 4 characters.
# 7. Display all words starting with a vowel.
# 8. Count the number of vowels and consonants.

message = "Python is awesome and Python is easy to learn"

print("Message: ", message)

# 1. Count total characters
total_characters = len(message)     #counting length of the message using len() function
print("Total characters: ", total_characters)

# 2. Count total words
words = message.split()     #counting total words by splitting the message into a list of words using split() function
print("Total words: ", len(words))

# 3. Find the longest word
#finding the longest word by using max() function with key as len to compare the length of each word
longest_word = max(words, key=len)    
print("Longest word: ", longest_word)

# 4. Find the shortest word
#finding the shortest word by using min() function with key as len to compare the length of each word
shortest_word = min(words, key=len)
print("Shortest word: ", shortest_word)

# 5. Count how many times the word "Python" appears
#counting the occurrences of the word "Python" in the message using count() function
python_count = message.count("Python")     
print("Count of 'Python': ", python_count)

# 6. Create a list of words having more than 4 characters
words_more_than_4 = []
for word in words:
    if len(word) > 4:
        words_more_than_4.append(word)
print("Words having more than 4 characters: ", words_more_than_4)

# 7. Display all words starting with a vowel
vowels="aeiou"
words_starting_with_vowel = []
#iterating through each word in the message, converting it to lowercase and checking if it starts with any of the vowels using startswith() function
for word in message.lower().split():   
    if word.startswith(tuple(vowels)): 
        words_starting_with_vowel.append(word)

print("Words starting with a vowel: ", words_starting_with_vowel)

# 8. Count the number of vowels and consonants
vowel_count = 0
consonant_count = 0
for char in message.lower():
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print("Number of vowels: ", vowel_count)
print("Number of consonants: ", consonant_count)





'''
Output:
Message:  Python is awesome and Python is easy to learn
Total characters:  49
Total words:  10
Longest word:  awesome
Shortest word:  is
Count of 'Python':  2
Words having more than 4 characters:  ['Python', 'awesome', 'easy']
Words starting with a vowel:  ['and']
Number of vowels:  12
Number of consonants:  27
'''