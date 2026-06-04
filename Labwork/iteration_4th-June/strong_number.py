#enter a number
number=int(input("enter the number:"))

#validating that number should not be negative
if(number<0):
     
     #exit from the execution 

     exit("number is negative....exited")

   #making a copy of the number  

temp=number

#initialisation of sum
sum=0


while(temp>0):

    #calculating digits of a number
    
    digit=temp%10

    #initialisation of factorial 

    fact=1

    #calculating factor of the digit
    for i in range(1,digit+1):
           fact=fact*i

     #calculating sum of the factors of the digit 
    sum=sum+fact

    #updating the number for next iteration
    
    temp=temp//10

    #checking the number is strong number or not 

if(number==sum):
    print(number,"is a strong number")
else:
    print(number,"is not a strong number")

