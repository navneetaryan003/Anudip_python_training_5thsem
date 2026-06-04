count=0

#enter the number
number=int(input("enter the number"))

#validate the number
if(number<0):
    exit("cannot be checked beacause number is negative")


while(True):

    #checking whether the number is prime or not 
    for i in range(1,number+1):
        if (number%i==0):
            count+=1

     #if number is prime then displaying       
    if(count==2):
        print(number,"is a prime number") 
        break    
    else:

        print(number,"is not prime")

        #factor is displaying if number is not prime 
        for i in range(1,number+1):
            if(number%i==0):
                print("Factors:",i)
        break        


    
    