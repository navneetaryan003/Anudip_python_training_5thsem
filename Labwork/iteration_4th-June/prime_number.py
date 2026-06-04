count=0

#enter the number
number=int(input("enter the number"))

#validate the number
if(number<0):

    #exit from the execution if number is less than zero
    
    exit("cannot be checked beacause number is negative")


while(True):

    #checking whether the number is prime or not 
    for i in range(2,(number//2)+1):
        if (number%i==0):
            count+=1      #counting how many times number is divisible 

     #if number is prime then displaying       
     
    if(count==0):
        print(number,"is a prime number") 
        break    
    else:

        print(number,"is not prime")

        #factor is displaying if number is not prime 
        for i in range(1,number+1): #number+1 specifies that loop goes to one less than mention

            if(number%i==0):

                print("Factors:",i) #printing factors of that number
        break        


    
    