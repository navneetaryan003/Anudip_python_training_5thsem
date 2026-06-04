
#an armstrong number is a number that is equal to the sum of its digit raised to the powers of the total number of digit 

#taking input a number
number=int(input("enter the number:"))


#making copy of the number
temp=number

#calculating digit in a number for calculating armstrong number 
#str is used to convert integer into string because integer cannot be calculated no of digits 

digits=len(str(number))

#initialiasation of sum 
sum=0

#calculating sum of the digit 
while(temp>0):

    digit=temp%10 #
    sum=sum+digit**digits
    temp=temp // 10

 #checking whether the number is armstrong or not    
if(number==sum):
    print(number,"is a armstrong number")
else:
    print(number,"is not armstrong number")