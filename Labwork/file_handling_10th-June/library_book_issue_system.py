# Library Book Issue System
# Problem Statement
# A library stores book information in books.txt.
# File Format
# B101,Python Basics,5
# B102,Java Programming,2
# B103,Data Science,0
# B104,DBMS,3
# B105,Machine Learning,1
# B106,Operating Systems,4
# B107,Networking,2
# B108,Cyber Security,6
# B109,Cloud Computing,0
# B110,Web Development,3
# Requirements
# Develop a program to:
# 1. Display all books.
# 2. Search a book using Book ID.
# 3. Issue a book (decrease quantity by 1).
# 4. Return a book (increase quantity by 1).
# 5. Display unavailable books.
# 6. Display books requiring restocking (copies < 2).
# 7. Update the file after every issue/return operation.


#---------------------------------------------------------------
file=open("Labwork/file_handling_10th-June/library_books.txt","r")


#menu driven program
print("1. Display all books")
print("2. Search a book using Book ID")
print("3. Issue a book (decrease quantity by 1)")
print("4. Return a book (increase quantity by 1)")
print("5. Display unavailable books")
print("6. Display books requiring restocking (copies < 2)")
print("7. Update the file after every issue/return operation")
print("8. Exit")

while True:
    choice=int(input("enter your choice"))

    if choice==1:
        print(file.read())

    elif choice==2:
        book_id=input("enter book id")
        for line in file:
            if book_id in line:
                print(line)

    elif choice==3:
        book_id=input("enter book id")
        for line in file:
            if book_id in line:
                quantity=int(line.split(",")[2])