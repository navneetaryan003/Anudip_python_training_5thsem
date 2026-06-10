# Movie Review Sentiment Analyzer
# Problem Statement
# Movie reviews are stored as follows:
# reviews = [
# "excellent movie",
# "average story",
# "excellent acting",
# "poor direction",
# "excellent visuals",
# "poor screenplay",
# "good music",
# "excellent climax",
# "average performance",
# "good cinematography"
# ]
# Requirements
# Create the following functions:
# 1. count_sentiments(reviews)
# Counts:
# • Excellent
# • Good
# • Average
# • Poor reviews
# 2. most_common_word(reviews)
# Returns the most frequently occurring word.
# 3. longest_review(reviews)
# Returns the review containing the maximum number of characters.
# 4. reviews_with_keyword(reviews, keyword)
# Displays all reviews containing a given keyword.

# Movie Review Sentiment Analyzer

reviews = [
"excellent movie",
"average story",
"excellent acting",
"poor direction",
"excellent visuals",
"poor screenplay",
"good music",
"excellent climax",
"average performance",
"good cinematography"
]


# Function to count sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for review in reviews:
        if "excellent" in review:
            excellent += 1
        elif "good" in review:
            good += 1
        elif "average" in review:
            average += 1
        else:
            poor += 1

    return excellent, good, average, poor


# Function to find the most common word
def most_common_word(reviews):
    word_frequency = {}

    for review in reviews:
        words = review.split()
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    
    most_common=max(word_frequency,key=word_frequency.get)
    return most_common

# Function to find the longest review
def longest_review(reviews):
    longest_review = reviews[0]
    for review in reviews:
        if len(review) > len(longest_review):
            longest_review = review
    return longest_review

# Function to display reviews with a given keyword
def reviews_with_keyword(reviews, keyword):
    found=False
    for review in reviews:
        if keyword in review:
            print(review)
            found=True
    if not found:
        print("No reviews found with the keyword.")
        
        
    
        
             


# Main program

#function calling for displaying sentiments
excellent, good, average, poor = count_sentiments(reviews)

#displaying sentiments
print("Excellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)

#for finding most common word

print("Most Common Word:", most_common_word(reviews))


# for finding longest review
print("Longest Review:", longest_review(reviews))


#for finding reviews with keyword
#ask user for keyword
keyword = input("Enter a keyword to search: ")

#validating keyword
if not keyword.replace(" ","").isalpha():
    print("Invalid keyword. Please enter a valid keyword.")
    exit()

else:
    reviews_with_keyword(reviews, keyword)