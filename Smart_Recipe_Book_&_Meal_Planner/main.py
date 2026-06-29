#main program for all modules 
from user_authentication import *
# from recipe import *
# from meal_planner import *
# from shopping_list import *
# from exception_handling_project import *


# Main program
while True:
    print("Welcome to Smart Recipe Book and Meal Planner")
    print("1.Login")
    print("2.Register")
    print("3.Change Password")

    # Take user's choice
    choice = input("Enter your choice: ")

    #checking the choice is integer or not
    if not choice.isdigit():
      print("Please enter a valid choice number")
      continue

    #converting the choice to integer
    choice=int(choice)


    #validate the choice
    if choice<1 or choice>3:
       print("invalid choice")
       continue

    # Call the corresponding module based on the user's choice
    if choice == 1:
      valid=login()
    elif choice == 2:
      valid = register()
    elif choice == 3:
      valid=change_password()

    # If login is not successful, prompt the user to try again
    if not valid:
      print("Invalid username or password. Please try again.")
    
    # If login is successful, break the loop
    if valid:
      break







