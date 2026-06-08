# A vehicle number plate is entered:
# MH12AB4589
# Tasks
# Write a program to:
# 1. Extract state code.
# 2. Extract district code.
# 3. Extract vehicle series.
# 4. Extract vehicle number.
# 5. Count letters and digits separately.
# 6. Verify:
# o First 2 characters must be alphabets.
# o Next 2 must be digits.
# o Next 2 must be alphabets.
# o Last 4 must be digits.
# 7. Display whether the number plate is valid.

number_plate = "MH12AB4589"
print("Number Plate:", number_plate)

# 1. Extract state code.
state_code = number_plate[0:2]
print("State Code:", state_code)

# 2. Extract district code.
district_code = number_plate[2:4]
print("District Code:", district_code)

# 3. Extract vehicle series.
vehicle_series = number_plate[4:6]
print("Vehicle Series:", vehicle_series)

# 4. Extract vehicle number.
vehicle_number = number_plate[-4:]
print("Vehicle Number:", vehicle_number)

# 5. Count letters and digits separately.
letters_count = 0
digits_count = 0
for char in number_plate:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1
print("Total Letters :", letters_count)
print("Total Digits :", digits_count)

# 6. Verify the format of the number plate.
is_valid = True
if not (number_plate[0:2].isalpha() and number_plate[0:2].isupper()):
    is_valid = False
if not number_plate[2:4].isdigit():
    is_valid = False
if not (number_plate[4:6].isalpha() and number_plate[4:6].isupper()):
    is_valid = False
if not number_plate[-4:].isdigit():
    is_valid = False


# 7. Display whether the number plate is valid.
if is_valid:
    print("Vehicle Number Status: Valid.")
else:   
    print("Vehicle Number Status: Invalid")


'''
output:
Number Plate: MH12AB4589
State Code: MH
District Code: 12
Vehicle Series: AB
Vehicle Number: 4589
Total Letters : 4
Total Digits : 6
Vehicle Number Status: Valid.
'''