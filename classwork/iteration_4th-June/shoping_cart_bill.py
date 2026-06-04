total_bill=0
while(True):
    
   item_added=int(input("enter item price"))
   
   if(item_added==0):
        break
   total_bill=total_bill+item_added
print("total bill ammount",total_bill)

