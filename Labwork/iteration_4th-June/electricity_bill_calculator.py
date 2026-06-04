#enter the electricity units that user consumed 
consumed_units=int(input("enter the consumed elecricity units :"))

#validate the consumed units
if(consumed_units<0):
    print("consumed units cannot be negative")

    #display the consumed units
print("units consumed",consumed_units)

#checking whether the consumption is high , moderate and low 
#also calculating the total bill of the user 

if(0<=consumed_units<=100):
    Total_bill=consumed_units*5
    print("Total Bill",Total_bill)
    print("Low")
elif(101<=consumed_units<=200):
    Total_bill=consumed_units*7
    print("Total Bill",Total_bill)
    print("Moderate") 
else:
    Total_bill=consumed_units*10
    print("Total bill:",Total_bill)
    print("High")