#copy a data from one file to another file

file1=open("classwork/file_handling_10th-June/sentences.txt","r")
if not file1:
    exit("file is not opened")


file2=open("classwork/file_handling_10th-June/copy.txt","w")

data=file1.read()

#check if file is empty
if not data:
    exit("file is empty")

#copy the data
file2.write(data)

print("data has been copied")

#close the file
file1.close()

#close the file
file2.close()