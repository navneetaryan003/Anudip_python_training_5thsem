#Area of triangle using heron's formula whose conditions are :
# 1. If the user enters a non-numeric value instead of a number for any side, display an appropriate error
# message.
# 2. If any of the entered side lengths are zero or negative, inform the user that triangle sides must be
# greater than zero.
# 3. If the three entered side lengths cannot form a valid triangle according to the Triangle Inequality
# Theorem, notify the user that the triangle is invalid.
# 4. Ensure that the program does not terminate abruptly due to invalid input and provides meaningful
# feedback using exception handling.
# 5. Display a message indicating that the triangle area calculation process has been completed,
#  regardless of whether the calculation was successful or an exception occurred.


#custom exception for negative value
class NegativevalueError(Exception):
    pass

#custom exception for traingle not formed
class TriangleError(Exception):
    pass


#to find area of triangle
try :
    a=int(input("Enter the first side of triangle: "))
    
    #handle the exception occurred in case of non-numeric value
    if not str(a).isnumeric():
        raise ValueError(f"input value {a} is invalid")
    
    #handle of negative value
    if a<0:
        raise NegativevalueError(f"input value {a} is negative")
    
    b=int(input("Enter the second side of triangle:"))
    
    #handle the exception occurred in case of non-numeric value
    if not str(b).isnumeric():
        raise ValueError(f"input value {b} is invalid")
    
    #handle of negative value
    if b<0:
        raise NegativevalueError(f"input value {b} is negative")
    
    c=int(input("Enter the third side of triangle: "))
    
    #handle the exception occurred in case of non-numeric value
    if not str(c).isnumeric():
        raise ValueError(f"input value {c} is invalid")
    
    #handle of negative value
    if c<0:
        raise NegativevalueError(f"input value {c} is negative")
    
    #check if these three sides form a triangle or not
    if a+b<=c or b+c<=a or c+a<=b: 
        raise TriangleError(f"triangle is not formed using these sides {a},{b},{c}")


#exception for non-numeric value
except ValueError as e:
    print(e)

#exception for negative value
except NegativevalueError as e:
    print(e)

#exception for traingle not formed
except TriangleError as e:
    print(e)

else:
    #to calculate area
    s=(a+b+c)/2
    print("area of circle is: ",(s*(s-a)*(s-b)*(s-c))**0.5)

#used for release resources
finally:

    print("triangle operation completed")

