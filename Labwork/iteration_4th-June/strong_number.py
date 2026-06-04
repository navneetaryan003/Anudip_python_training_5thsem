#enter a number
number=int(input("enter the number:"))
if(number<0):
     exit("number is negative....exited")

temp=number
sum=0


while(temp>0):

    #calculating digits of a number
    
    digit=temp%10
    fact=1

    #calculating factor of the digit
    for i in range(1,digit+1):
           fact=fact*i

     #calculating sum of the factors of the digit
     #       
    sum=sum+fact
    temp=temp//10

    #checking the number is strong number or not 

if(number==sum):
    print(number,"is a strong number")
else:
    print(number,"is not a strong number")

