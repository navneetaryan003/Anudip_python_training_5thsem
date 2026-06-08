# Password Strength Analyzer
# Problem Statement
# A user enters a password.
# Python@2026!
# Tasks
# Write a program to determine whether the password is Strong, Medium, or Weak.
# Rules:
# • Minimum length 8
# • Contains at least:
# o 1 uppercase letter
# o 1 lowercase letter
# o 1 digit
# o 1 special character
# Additionally:
# 1. Count uppercase letters.
# 2. Count lowercase letters.
# 3. Count digits.
# 4. Count special characters.
# 5. Display all digits separately.
# 6. Display all special characters separately.

password = "Python@2026!"

# Check password strength
if len(password) < 8:     # Minimum length check
    print("Weak Password")

else:

    uppercase_count = 0    # Count uppercase letters
    lowercase_count = 0    # Count lowercase letters
    digit_count = 0        # Count digits
    special_char_count = 0   # Count special characters
    digits = []             # List to store digits
    special_chars = []     # List to store special characters

    for char in password:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
            digits.append(char)
        else:
            special_char_count += 1
            special_chars.append(char)

    if uppercase_count >= 1 and lowercase_count >= 1 and digit_count >= 1 and special_char_count >= 1:
        print("Strong Password")
    else:
        print("Medium Password")

    print(f"Uppercase Letters: {uppercase_count}")
    print(f"Lowercase Letters: {lowercase_count}")
    print(f"Digits: {digit_count} - {', '.join(digits)}")
    print(f"Special Characters: {special_char_count} - {', '.join(special_chars)}")


'''
Output:
Strong Password
Uppercase Letters: 1
Lowercase Letters: 5
Digits: 4 - 2, 0, 2, 6      
Special Characters: 1 - @

'''