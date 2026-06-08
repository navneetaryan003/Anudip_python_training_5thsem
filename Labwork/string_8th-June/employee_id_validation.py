# ------------ Employee ID Validation and Analysis System-----------------
# Problem Statement
# A company generates employee IDs in the following format:
# EMP2026ANUJ458
# Tasks
# Write a program to:
# 1. Count the number of uppercase letters.
# 2. Count the number of digits.
# 3. Extract the joining year.
# 4. Extract the employee name.
# 5. Check whether the ID follows these rules:
# o Starts with "EMP"
# o Contains exactly 4 digits for the year
# o Ends with exactly 3 digits
# 6. Create a list containing all digits present in the ID.
# 7. Find the sum of all digits present in the ID.
# 8. Display whether the ID is valid or invalid.

emp_id = "EMP2026ANUJ458"

# 1. Count the number of uppercase letters.
uppercase_count=0
for char in emp_id:
    if char.isupper():
        uppercase_count+=1

print("Number of uppercase letters:", uppercase_count)

# 2. Count the number of digits.
digit_count=0
for char in emp_id:
    if char.isdigit():
        digit_count+=1

print("Number of digits:", digit_count)

# 3. Extract the joining year.
joining_year = " "
if emp_id.startswith("EMP"):
    for char in emp_id[3:7]:
        if char.isdigit():
            joining_year+=char

print("Joining year:", joining_year)

# 4. Extract the employee name.
employee_name = " "
if emp_id.startswith("EMP"):
    for char in emp_id[7:-3]:
        if char.isalpha():
            employee_name+=char

print("Employee name:", employee_name)

# 5. Check whether the ID follows these rules:

# o Starts with "EMP"
is_valid = True
if not emp_id.startswith("EMP"):
    is_valid = False

# o Contains exactly 4 digits for the year
if not emp_id[3:7].isdigit():
    is_valid = False
if not emp_id[7].isalpha():
    is_valid = False

# o Ends with exactly 3 digits
if not emp_id[-3:].isdigit() or not emp_id[-4].isalpha():
    is_valid = False

print("ID is valid:", is_valid)

# 6. Create a list containing all digits present in the ID.
digits_list = []
for char in emp_id:
    if char.isdigit():
        digits_list.append(char)

print("List of digits in the ID:", digits_list)

# 7. Find the sum of all digits present in the ID.
digits_sum = 0
for char in emp_id:
    if char.isdigit():
        digits_sum += int(char)

print("Sum of all digits in the ID:", digits_sum)


# 8. Display whether the ID is valid or invalid.
if is_valid:
    print("The ID is valid.")
else:    
    print("The ID is invalid.")


'''Output:
Number of uppercase letters: 7

Number of digits: 7
Joining year: 2026
Employee name: ANUJ
ID is valid: True
List of digits in the ID: ['2', '0', '2', '6', '4', '5', '8']
Sum of all digits in the ID: 27
The ID is valid.
'''
