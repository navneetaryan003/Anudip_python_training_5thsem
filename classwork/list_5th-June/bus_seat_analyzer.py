#write a program to analyze the available and booked seats in bus

seats=[1,0,1,1,0,0,1,1,1,0]

booked=0   #iniliasation of booked seats 

available=0   #initialisation of available seats 

available_seats=[]     #creating a list for available seats record 

for i in range(len(seats)):

    if(seats[i]==1):
        booked+=1    #counting booked seats in a bus 

    else:
        available+=1    #countin available seats in a bus 
        available_seats.append(i+1)    #adding available seats 


for i in range(len(seats)):
     
     if(seats[i]==0):          #calculating the first available seats in the bus 
        first_available=i+1
        break

occupied=(booked/len(seats))*100   #calculting how much seats are occupied 

print("Booked Seats",booked)

print("Available Seats",available)

print("First Available Seats",first_available)

print("Available Seat Number",available_seats)

print("Bus occupancy:",occupied,"%")


#checking whether the seat occupied is more than 70 percent or not 

if(occupied>70):
    print("more than 70% occupied")
else:
    print("not more than 70% occupied")
    