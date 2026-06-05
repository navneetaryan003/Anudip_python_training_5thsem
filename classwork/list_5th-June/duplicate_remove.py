#program to remove duplicate entries of given number

numbers=[] #take a empty list

for i in range(20):

    num=int(input("enter the number")) #taking input from user 

    numbers.append(num)     #add them to the list

diff_number=int(input("enter the another number:"))   #taking different number from the user 


counts=numbers.count(diff_number)     #count the target number how many times it occured 


if(counts==0):
    print(diff_number ,"is not found")


elif(counts==1):
    print("no duplicates found")
    

else:    

    #reversing the list
    numbers.reverse()
    for i in range(1,counts):

        # removing the duplicate element
        numbers.remove(diff_number)
    
    numbers.reverse() #again reversing the list to make it in original form 

print(numbers)
    



