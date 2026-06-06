# Write a Python program to:
# 1. Display all passengers whose booking status is Confirmed.
# 2. Count the number of passengers travelling to Delhi.
# 3. Count Confirmed, Waiting, and Cancelled bookings separately.
# 4. Create a list containing passenger IDs with Waiting status.
# 5. Determine which destination has the highest number of bookings.


#booking details
bookings = (
("P101", "Delhi", "Confirmed"),
("P102", "Mumbai", "Waiting"),
("P103", "Delhi", "Confirmed"),
("P104", "Chennai", "Cancelled"),
("P105", "Mumbai", "Confirmed"),
("P106", "Delhi", "Waiting")
)

#counters used for counting or tracking 

count_delhi=0  #for counting who travelled to delhi

count_confirmed=0  #for counting confirmed booking

count_waiting=0     #for counting waiting booking

count_cancelled=0    #for counting cancelled booking

delhi=0         #for counting the number of passengers going to delhi

mumbai=0        #for counting the number of passengers going to mumbai

chennai=0       #for counting the number of passengers going to chennai

#list for collecting booking details
waiting_list=[]      #for holding data of passengers who are in waiting list

for record in bookings:

    #task 1.To display all passengers whose booking status is Confirmed.
    #task3 : To count Confirmed, Waiting, and Cancelled bookings separately.

    if record[2]=="Confirmed":
        print(record[0],record[1])
        count_confirmed+=1

    
    elif record[2]=="Waiting":
        count_waiting+=1

        #task4: To  create a list containing passenger IDs with Waiting status.
        waiting_list.append(record[0])
    
    else:
        count_cancelled+=1

    

    #task2: To count the number of passengers travelling to Delhi.
    # task5:To determine which destination has the highest number of bookings.
    if record[1]=="Delhi":
        count_delhi+=1
        delhi+=1


    
    elif record[1]=="Mumbai":
        mumbai+=1
    
    else:
        chennai+=1


print("------------------------------")
print("Passengers Travelling to Delhi:",count_delhi)

print("-------------------------------")
print("Confirmed:",count_confirmed)
print("waiting:",count_waiting)
print("cancelled:",count_cancelled)

print("-------------------------------")
print("Waiting List:",waiting_list)

print("--------------------------------")
print("Most Booked Destination:")

#checking which destination visited most 

if delhi>mumbai and delhi>chennai:
    print("Delhi")

elif chennai>delhi and chennai>mumbai:
    print("Chennai")

else:
    print("Mumbai")
    