# License Key Verification System
# Problem Statement
# A software license key is entered:
# ABCD-EFGH-IJKL-MNOP
# Tasks
# Write a program to:
# 1. Verify there are exactly 4 groups.
# 2. Verify each group contains exactly 4 characters.
# 3. Count total letters.
# 4. Count vowels.
# 5. Remove hyphens and display the merged key.
# 6. Create a list containing all groups.
# 7. Display whether the key format is valid.

# License Key Verification System

license_key = "ABCD-EFGH-IJKL-MNOP"

print("License Key:")
print(license_key)

# Create list of groups
groups = license_key.split("-")

print("\nGroups:")
print(groups)

# Verify format
is_valid = True

# Check number of groups
if len(groups) != 4:
    is_valid = False

# Check each group length
for group in groups:
    if len(group) != 4:
        is_valid = False

# Remove hyphens
merged_key = license_key.replace("-", "")

# Count total letters
total_letters = len(merged_key)

# Count vowels
vowel_count = 0

for ch in merged_key:
    if ch in "AEIOU":
        vowel_count += 1

# Display results
print("\nNumber of Groups:", len(groups))
print("Total Letters:", total_letters)
print("Total Vowels:", vowel_count)

print("\nMerged Key:")
print(merged_key)

# Status
if is_valid:
    print("\nLicense Key Status: Valid")
else:
    print("\nLicense Key Status: Invalid")