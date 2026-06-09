#write a program which provides menu to user for selecting two dimensional figure (square, rectangle, circle) and after selecting the figure user is again asked to provide the input of corresponding the data for the figure and after that again providing the menu to select operation (area or perimeter) and the task will be repeated untill user choose exit option and this will done using custom module import 

#import the module
from area_and_perimeter import *

#creating a function for choosing operation
def choose_operation():
    
    operation=int(input("enter the operation you want to perform (1.area 2.perimeter):"))

    #validate the operation
    if operation<1 or operation>2:
        exit("invalid operation")
    
    return operation

#main program
while(True):
    print("1.square")
    print("2.rectangle")
    print("3.circle")
    print("4.exit")
    choice=int(input("enter your choice for figure:"))

    #validate the choice
    if choice<1 or choice>4:
        exit("invalid choice")
    
    #to exit
    if choice==4:
        break

    

    if(choice==1):
        side=float(input("enter the side of square:"))

        #validate the side
        if side<=0:
            exit("side cannot be negative or zero")

        #to choose operation
        operation=choose_operation()
        
        #to calculate area of square
        if operation==1:
            print("area of square:",square_area(side))

        #to calculate perimeter of square    
        elif operation==2:
            print("perimeter of square:",square_perimeter(side))

    elif(choice==2):
        length=float(input("enter the length of rectangle:"))

        #validate the length
        if length<=0:
            exit("length cannot be negative or zero")


        breadth=float(input("enter the breadth of rectangle:"))

        #validate the breadth
        if breadth<=0:
            exit("breadth cannot be negative or zero")
        
        #to choose operation
        operation=choose_operation()

        #to calculate area of rectangle
        if operation==1:
            print("area of rectangle:",rectangle_area(length,breadth))

        #to calculate perimeter of rectangle    
        elif operation==2:
            print("perimeter of rectangle:",rectangle_perimeter(length,breadth))

    elif(choice==3):
        radius=float(input("enter the radius of circle:"))

        #validate the radius
        if radius<=0:
            exit("radius cannot be negative or zero")
        
        #to choose operation
        operation=choose_operation()

        #to calculate area of circle
        if operation==1:
            print("area of circle:",circle_area(radius))

        #to calculate perimeter of circle    
        elif operation==2:
            print("perimeter of circle:",circle_circumference(radius))

    


    
    
    

