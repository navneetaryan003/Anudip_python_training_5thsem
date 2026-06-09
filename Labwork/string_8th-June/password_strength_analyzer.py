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

password = input("enter the password :")  # Example password   
print(f"Password: {password}")

if password.isspace():
    exit("password cannot be empty")

# Check password strength
if len(password) < 8:     # Minimum length check
    print("Weak Password")

else:

    uppercase_count = 0    # Count uppercase letters
    lowercase_count = 0    # Count lowercase letters
    digit_count = 0        # Count digits
    special_char_count = 0   # Count special characters

    if password.isdigit():
         digits = []      # List to store digits

    
    special_chars = []     # List to store special characters

    for char in password:
        if char.isupper():     # Check for uppercase letters
            uppercase_count += 1

        elif char.islower():     # Check for lowercase letters
            lowercase_count += 1

        elif char.isdigit():     # Check for digits
            digit_count += 1
            digits.append(char)    # Store the digit separately
        else:
            special_char_count += 1       # Check for special characters
            special_chars.append(char)   # Store the special character separately

    

    print(f"Uppercase Letters: {uppercase_count}")
    print(f"Lowercase Letters: {lowercase_count}")
    print(f"Digits: {digit_count}")
    print(f"Special Characters: {special_char_count} ")
    print("Digits:  ",digits)
    print("Special Characters:  ", special_chars)

    
    # Determine password strength based on the counts
    conditions=0
    if uppercase_count:
        conditions+=1
    
    if lowercase_count:
        conditions+=1
    
    if digit_count:
        conditions+=1

    if special_char_count:
        conditions+=1

    if conditions==4:
        print("Password Strength : Strong")
    elif conditions>=2:
        print("Password Strength : Medium")
    else:
        print("Password Strength : Weak")


'''
Output:
Password: Python@2026!
Uppercase Letters: 1
Lowercase Letters: 5
Digits: 4 - 2, 0, 2, 6      
Special Characters: 1 - @
Password Strength : Strong

'''