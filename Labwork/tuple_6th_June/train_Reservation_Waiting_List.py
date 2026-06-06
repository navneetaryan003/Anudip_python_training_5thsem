# Write a program to:
# • Display all waiting-list passengers.
# • Count confirmed and waiting passengers.
# • Find whether a specific passenger has a confirmed ticket.
# • Create separate lists for confirmed and waiting passengers.

#details of passenger
passengers = [
("Anuj", "Confirmed"),
("Rahul", "Waiting"),
("Priya", "Confirmed"),
("Amit", "Waiting"),
("Neha", "Confirmed")
]


count_confirmed=0    #for counting confirmed tickets
count_waiting=0      #for counting waiting tickets 

confirmed_list=[]    #list for confirmed tickets
waiting_list=[]      #list for waiting tickets


for passenger in passengers:

    
    
   

    if passenger[1]=="Waiting":

        #task 1 :Display all waiting-list passengers.

        print(passenger[0])

        #task 2 :Count confirmed and waiting passengers.
        count_waiting+=1

        #task 4 : Create separate lists for confirmed and waiting passengers.
        waiting_list.append(passenger[0])
    
    else:
        count_confirmed+=1
        confirmed_list.append(passenger[0])

print("number of Confirmed passengers : ",count_confirmed)
print("number of Waiting passenger :",count_waiting)

#task 3:  Find whether a specific passenger has a confirmed ticket.

passenger_find=input("enter the passenger name :")

for name , status in passengers:
    if passenger_find.capitalize()==name:
        if status=="Confirmed":
            print(passenger_find," has a confirmed ticket")
            break
        
        else:
            print(passenger_find," has not confirmed tickets")
            break
    
else:
        print(passenger_find,"has not found in list")


print("confirmed passengers list :",confirmed_list)

print("waiting passengers list :",waiting_list)


