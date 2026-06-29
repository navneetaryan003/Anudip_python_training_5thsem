from exception_handling_project import *


#user authentication for login , registration and change password using passing user name and password from main program 

special_characters="!@#$%^&*()_+-=[]{}|;:,.<>/?"

max_tries=3

min_length=4

max_length=15

# function to validate user name
def validate_user_name(user_name):

     #validating the user name
    if not user_name:
        print("user_name is not empty")
        return False

    #checking if username starts with a letter
    if not user_name[0].isalpha():
        print("username should start with a letter")
        return False

    #checking the user_name length
    if len(user_name) > max_length:
        print("username should have at most 15 characters")
        return False
    
    if len(user_name) < min_length:
        print("username should have at least 4 characters")
        return False
    
    #checking if username contains only letters , numbers and underscores
    if not user_name.replace("_","").isalnum():
        print("username should contain only letters ,numbers and underscores")
        return False

    #returning true to verify the user name
    return True
#-----------------------------------------------------------------------------------------------------------------------------------
#function to validate password
def validate_password(password):

    #validating the password
    if not password:
        print("password is not empty")
        return False

    #checking the password length
    if len(password) > max_length:
        print("password should have at most 15 characters")
        return False
    
    if len(password) < min_length:
        print("password should have at least 8 characters")
        return False
    
    #checking if password contains one uppercase letter
    if not any(char.isupper() for char in password):
        print("password should contain at least one uppercase letter")
        return False

    #checking if password contains one lowercase letter
    if not any(char.islower() for char in password):
        print("password should contain at least one lowercase letter")
        return False

    #checking if password contains one digit
    if not any(char.isdigit() for char in password):
        print("password should contain at least one digit")
        return False
    
    #checking if password contains one special character


    if not any(char in special_characters for char in password):
        print("password should contain at least one special character")
        return False

    #returning true to verify the password
    return True

#--------------------------------------------------------------------------------------------------------------------------------
#function to get valid user name
def get_valid_username():
    
    counter=0
    
    while counter < max_tries:

        #taking user name from the user
        user_name=input("enter user_name :").strip()
        

        #validating the user name
        if validate_user_name(user_name):
            return user_name

        counter+=1
        
    if counter==max_tries:
            print("You have entered invalid user name 3 times")
            return None
        
#--------------------------------------------------------------------------------------------------------------------------------
#function to get valid password
def get_valid_password():
    
    counter=0
    

    while counter < max_tries:

        #taking password from the user
        password=input("enter password :").strip()

        #validating the password
        if validate_password(password):
            return password

        counter+=1
        
    if counter==max_tries:
      print("You have entered invalid password 3 times")
      return None
    

#-------------------------------------------------------------------------------------------------------------------------------
#login  Function
def login():
    
    user_name=get_valid_username()

    if user_name is None:
        print("Too many attempts")
        return False

    password=get_valid_password()

    if password is None:
        print("Too many attempts")
        return False
    

    #reading the users.txt file
    file=open_file(r"Smart_Recipe_Book_&_Meal_Planner\uers.txt" , "r")

    if file is None:
        return False

    file.seek(0)
    with file: 

        for line in file:

            #splitting the line into username and hashed password
            username , stored_password = line.strip().split(":")

            #checking if the username and password match
            if user_name == username and stored_password == password:
                        print(f"Welcome , {user_name}")

                        #returning true to verify the login
                        return True
        
    print("Invalid username or password")
    #returning false to verify the login
    return False

#-------------------------------------------------------------------------------------------------------------------------------

#registration
def register():
    
    user_name=get_valid_username()

    if user_name is None:
        print("Too many attempts")
        return False
    

    #checking if the user name already exists
    file=open_file(r"Smart_Recipe_Book_&_Meal_Planner\uers.txt" , "a+")

    if file is None:
        return False

    
       
    file.seek(0)
    
    with file:

        for line in file:

            #splitting the line into username and hashed password
            username , stored_password = line.strip().split(":")

            #checking if the username already exists
            if user_name == username:
                print(f"{user_name} already exists")
                return False

        password=get_valid_password()

        if password is None:
            print("Too many attempts")
            return False

        #writing the username and hashed password
        file.write(f"{user_name}:{password}\n")

        print(f"Welcome , {user_name}")

        #returning true to verify the registration
        return True


#-------------------------------------------------------------------------------------------------------------------------------
#change password
def change_password():
     
     user_name=get_valid_username()
     
     #checking whether the validating user name is correct or not
     if user_name is None:
        print("Too many attempts")
        return False

     current_password = get_valid_password()
     
     #checking whether the validating password is correct or not
     if current_password is None:
        print("Too many attempts")
        return False
     
     #creating a list named users to store the username and stored password
     users=[]
     
     #creating a boolean variable named found
     found=False
     
     #reading the users.txt file
     file=open_file(r"Smart_Recipe_Book_&_Meal_Planner\uers.txt" , "r")

     if file is None:
        return False

     file.seek(0)
     with file:

         for line in file:

             #splitting the line into username and hashed password
             username , stored_password = line.strip().split(":")

             #checking if the username and password match
             if user_name == username and stored_password == current_password:
                 
                 print("Enter new password")

                 new_password=get_valid_password()

                 if new_password is None:
                     print("Too many attempts")
                     return False
                 
                 #adding the username and new password into a list named users
                 users.append(f"{user_name}:{new_password}\n")
                 found=True
                 break
             
             else:
                 users.append(line)

        
     if not found:
        print("Invalid username or password")
        return False

     file=open_file(r"Smart_Recipe_Book_&_Meal_Planner\uers.txt" , "w")

     if file is None:
        return False

     
     with file:
         file.writelines(users)

     print("Password changed successfully")
     return True
                 
                 


     
         

    
     
   
     
     
    


