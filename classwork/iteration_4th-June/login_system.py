#validation of password 

correct_password="admin123"    #initialisation of correct password 

while(True):

    password=input("enter password")  #password enter by the user for validation

    if(password==correct_password):   #checking whether the password is matched or not 
        
        print("login successful")
        break
    else:
        print("invalid password")