#write a program to find consecutive pairs in a list

numbers=[4, 5, 6, 10, 11, 15, 16, 17]

consecutive_numbers=[]  #taking a empty list that store consecutive pairs 

for i in range(len(numbers)-1):
     
     if(numbers[i+1]-numbers[i]==1):  #checking the number is consecutive or not 
          
          print(numbers[i],"and",numbers[i+1],"are consecutive")

           #adding pairs to the empty list which are consecutive 
           
          consecutive_numbers.append((numbers[i],numbers[i+1]))

print(consecutive_numbers)

          