# Product Review Analyzer
# Problem Statement
# A customer submits a review:
# This product is excellent excellent excellent and very useful
# Tasks
# Write a program to:
# 1. Count total words.
# 2. Create a dictionary containing word frequencies.
# 3. Find the most frequently used word.
# 4. Find all words appearing only once.
# 5. Count words having more than 5 characters.
# 6. .Display words in reverse order
# 7. Create a list of unique words.

review="This product is excellent excellent excellent and very useful"

#1.Count total words.
words=review.split()
print("Total Words :",len(words))

#2.Create a dictionary containing word frequencies.
word_frequency={}
for char in words:
    if char in word_frequency:
        word_frequency[char]+=1
    
    else:
        word_frequency[char]=1

print("Word frequencies :")
for char , value in word_frequency.items():
    print(char,"->",value)

#3.displaying most frequent word 
print("Most Frequent Word:",max(word_frequency,key=word_frequency.get))


#4.all words that appearing once
appear_one=[]
for char , value in word_frequency.items():
    if value==1:
        appear_one.append(char)

print("Words Appearing Once :",appear_one)

#5.Count words having more than 5 characters.
count=0
for char in words:
    if len(char) >=5:
        count+=1
print("Number of words greater than 5 letters :",count)


#6.Display words in reverse order
print("Reversed order :")
for word in words[::-1]:
    print(word , end=" ")


unique_word=[]
for char in word_frequency.keys():
    unique_word.append(char)

print("\nUnique Words:",unique_word)




