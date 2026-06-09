# Username Generator System
# Problem Statement
# A student enters:
# Rahul Sharma
# Tasks
# Generate a username using the rules:
# 1. Remove spaces.
# 2. Convert to lowercase.
# 3. Append current year (2026).
# 4. If username length exceeds 12, keep only first 12 characters.
# 5. Count vowels in the generated username.
# 6. Count consonants.
# 7. Display username statistics.

# Username Generator System

name = input("Enter Name: ").strip()

if not name:
    exit("name cannot be empty")

# Remove spaces
username = name.replace(" ", "")

# Convert to lowercase
username = username.lower()

# Append current year
username = username + "2026"

# Keep only first 12 characters if length exceeds 12
if len(username) > 12:
    username = username[:12]

# Count vowels and consonants
vowel_count = 0
consonant_count = 0

vowels = "aeiou"

for ch in username:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Display output
print("\nOriginal Name:", name)
print("Generated Username:", username)
print("Username Length:", len(username))
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Status: Username Generated Successfully")