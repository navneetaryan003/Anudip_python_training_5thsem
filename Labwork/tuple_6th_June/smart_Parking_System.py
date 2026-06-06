# Write a program to:
# • Count occupied and available slots.
# • Find the first available slot.
# • Display all available slot numbers.
# • Check whether parking occupancy exceeds 75%.

#details of booking where 1 = Occupied and  0 = Available

slots = [1, 0, 1, 1, 0, 0, 1, 0]

occupied=0     #counter for counting occupied seats 
available=0     #ounter for counting available seats 

available_seat_slot=[]


for i in range(len(slots)):

    #task 1: Count occupied and available slots

    if slots[i]==1:
        occupied+=1
    else :
        available+=1

        #task 3 :Display all available slot numbers.
        available_seat_slot.append(i+1)

print("Occupied Seats :",occupied)
print("Available Seats :",available)

#task2 :Find the first available slot.

for i in range(len(slots)):
    if slots[i]==0:
        available_seat=i+1
        break

print("First available seat :",available_seat)

print("available seat slot :",available_seat_slot)

#task 4: Check whether parking occupancy exceeds 75%.

occupancy=(occupied/len(slots))*100
if occupancy>75:
    print("parking occupancy exceeds 75%")

else:
    print("parking occupancy does not exceeds 75%")




