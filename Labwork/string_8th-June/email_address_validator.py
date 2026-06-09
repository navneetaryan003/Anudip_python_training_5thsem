# Email Address Validator
# Problem Statement
# A user enters an email address:
# rahul.sharma2026@gmail.com
# Tasks
# Write a program to:
# 1. Extract username.
# 2. Extract domain name.
# 3. Extract extension.
# 4. Count digits present in username.
# 5. Count special characters.
# 6. Check whether:
# o Exactly one '@' exists.
# o At least one '.' exists after '@'.
# 7. Display Valid Email or Invalid Email.

email="rahul.sharma2026@gmail.com"


# 1. Extract username.
username=email.split("@")[0]
print("Username :",username)


#2. Extract domain name.
domain_name=(email.split("@")[1]).split(".")[0]
print("Domain name :",domain_name)


#3. Extract extension.
extension=(email.split("@")[1]).split(".")[1]
print("Extension :",extension)


#4. Count digits present in username.
count=0
for ch in username:
    if ch.isdigit():
        count+=1
print("Digits :",count)

#5. Count special characters.
count_special=0
for ch in email:
    if not ch.isalnum():
        count_special+=1

print("number of special characters",count_special)

#6. Check whether:
# o Exactly one '@' exists.
# o At least one '.' exists after '@'.
is_valid = True

# Exactly one @
if email.count("@") != 1:
    is_valid = False

# At least one . after @
else:
    at_pos = email.find("@")

    if "." not in email[at_pos + 1:]:
        is_valid = False

# 7. Display Valid Email or Invalid Email.
if is_valid:
    print("Email status : Valid")
else:
    print("Email Status : Invalid")

