#enter the electricity units that user consumed 
consumed_units=int(input("enter the consumed elecricity units :"))

#validate the consumed units if it is negative

if(consumed_units < 0):
    print("consumed units cannot be negative")

    #display the consumed units

print("units consumed",consumed_units)

#checking whether the consumption is high , moderate and low 
#also calculating the total bill of the user 

if(consumed_units<=100):

    Total_bill=consumed_units*5

    print("Total Bill",Total_bill) #displaying bill 
    print("Low Consumed")

elif(consumed_units<=200):

    Total_bill=100*5+((consumed_units-100)*7)

    print("Total Bill",Total_bill) #displaying bill
    print("Moderate consumed") 
    
else:
    Total_bill=(100*5)+(100*7)+((consumed_units-200)*10)

    print("Total bill:",Total_bill) #displaying bill
    
    print("High consumed")