# Text Compression Analyzer
# Problem Statement
# A compressed message is given:
# AAABBBCCCDDDAAA
# Tasks
# Write a program to:
# 1. Count occurrences of each character.
# 2. Create a dictionary of character frequencies.
# 3. Display unique characters.
# 4. Find the most frequent character.
# 5. Create a compressed output:
# A3B3C3D3A3
# 6. Calculate compression ratio.

# Text Compression Analyzer

text = "AAABBBCCCDDDAAA"

print("Original Text:")
print(text)

# Count frequencies
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Display frequencies
print("\nCharacter Frequencies:")

for key, value in freq.items():
    print(key, "->", value)

# Unique characters
unique_chars = list(freq.keys())

print("\nUnique Characters:")
print(unique_chars)

# Most frequent character
most_frequent = max(freq, key=freq.get)

print("\nMost Frequent Character:", most_frequent)

# Create compressed output
compressed = ""

current_char = text[0]
count = 1

for i in range(1, len(text)):

    if text[i] == current_char:
        count += 1

    else:
        compressed += current_char + str(count)

        current_char = text[i]
        count = 1

# Add last group
compressed += current_char + str(count)

print("\nCompressed Output:")
print(compressed)

# Compression ratio
original_length = len(text)
compressed_length = len(compressed)

compression_ratio = (compressed_length / original_length) * 100

print("\nOriginal Length:", original_length)
print("Compressed Length:", compressed_length)

print(f"\nCompression Ratio: {compression_ratio:.2f}%")