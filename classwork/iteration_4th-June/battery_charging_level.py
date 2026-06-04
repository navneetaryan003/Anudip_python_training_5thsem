#track the battery charging percentage 

charging_level=20        #initialisation of initial battery percentage 


while (charging_level<=100):

    print("battery level:",charging_level,"%") #displaying current charging percentage

    charging_level=charging_level+10    #increment in charging in every cycle 
    
print("battery full charged")