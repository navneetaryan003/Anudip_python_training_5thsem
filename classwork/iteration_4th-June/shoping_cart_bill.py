#write a program to track or calculate the bill of the user 

total_bill=0   #initialisation of bill ammount

while(True):
    
   item_added=int(input("enter item price"))  #taking price of item that is added
   
   if(item_added==0):        #checking whether it is zero priced enetr by the user to exit 
        break
   
   total_bill=total_bill+item_added   #calculating total bill untill user enter zero pricing in the cart
   
print("total bill ammount",total_bill)

