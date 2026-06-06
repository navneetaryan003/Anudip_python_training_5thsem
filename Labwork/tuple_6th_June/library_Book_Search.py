# Write a program to:
# • Display unavailable books.
# • Find all books with more than 2 copies.
# • Count available books.
# • Stop searching once a requested book is found.


#details of books avaialble in library 
books = [
("Python Basics", 5),
("Data Science", 0),
("Java Programming", 3),
("Machine Learning", 0)
]

more_books=[]  #creating empty list to store books that are more than 2 copies

count_available=0    #counter for counting available books

print("Unavailable books :")
for book in books:

    #task 1: Display unavailable books.
    if book[1]==0:
        print(book[0])
    
    #task 3: Count available books.
    else:
        count_available+=1
    
    #task 2 : Find all books with more than 2 copies.
    if book[1]>2:
        more_books.append(book[0])

searched_book=input("enter the book that you want : ")    #taking input for book to be searched 

#task 4 : Stop searching once a requested book is found.

for book in books:
    if book[0].title()==searched_book.title():
        print("book found")
        print("copies available :",book[1])
        break
    
else:
        print("book not found")


    




