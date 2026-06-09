#creating module for calculating area and perimeter of square , rectangle and circle

#function to calculate area  of square
def square(side):
    area=side*side
    return area

#function to calculate perimeter of square
def perimeter(side):
    perimeter=4*side
    return perimeter

#function to calculate area of rectangle
def rectangle(length,breadth):
    area=length*breadth
    return area

#function to calculate perimeter of rectangle
def perimeter(length,breadth):
    perimeter=2*(length+breadth)
    return perimeter

#function to calculate area of circle
def circle(radius):
    area=3.14*radius*radius
    return area 

#function to calculate circumference of circle
def circumference(radius):
    circumference=2*3.14*radius
    return circumference

