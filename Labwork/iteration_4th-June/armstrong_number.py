#checking for armstrong number
#taking input a number
number=int(input("enter the number:"))
temp=number

#calculating digit in a number
digits=len(str(number))
sum=0

#calculating sum of the digit 
while(temp>0):
    digit=temp%10
    sum=sum+digit**digits
    temp=temp // 10

 #checking whether the number is armstrong or not    
if(number==sum):
    print(number,"is a armstrong number")
else:
    print(number,"is not armstrong number")