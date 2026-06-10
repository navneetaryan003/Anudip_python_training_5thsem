#write a program to input 10 sentences from the user and store them in a file.

file = open("classwork/file_handling_10th-June/sentences.txt", "w")  # Open the file in write mode

print("Enter 10 sentences:")     # Prompt the user to enter 10 sentences

#loop to get 10 sentences
for i in range(1, 11):

    # Get the sentence from the user
    sentence = input()
    
    # Add a newline character at the end of the sentence
    sentence += "\n"

    # Write the sentence to the file
    file.write(sentence)
    
print("------------------------------------------------")

print("Data has been written to sentences.txt")

# Close the file
file.close()