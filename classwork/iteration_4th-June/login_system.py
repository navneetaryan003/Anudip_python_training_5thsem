correct_password="admin123"
while(True):
    password=input("enter password")
    if(password==correct_password):
        print("login successful")
        break
    else:
        print("invalid password")