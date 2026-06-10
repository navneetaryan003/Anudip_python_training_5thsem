# Classwork : To read the data from file and display the following:
# 1. No. of Vowels in file.
# 2. No. of characters into the file.
# 3. No. of lines into the file.

file=open("classwork/file_handling_10th-June/sentences.txt","r")

#validation of file

if file:
    print("file is opened")
else:
    print("file is not opened")

#reading data from file
data=file.read()
data=data.lower()


#no of vowels in file
vowels_count=0
for i in data:
    if i in "aeiou":
        vowels_count+=1

print("no of vowels in file : ",vowels_count)

#no of characters in file
lines=data.count("\n")
print("no of characters in file : ",len(data)-lines)

#no of lines in file
print("no of lines in file : ",lines)

#closing file
file.close()