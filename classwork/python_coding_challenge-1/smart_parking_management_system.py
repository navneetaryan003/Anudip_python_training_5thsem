# Smart Parking Management System
# Problem Statement
# The parking status of vehicles in a mall is maintained as follows.
# Sample Data
# parking_slots = [
# "Occupied", "Vacant", "Occupied", "Vacant",
# "Occupied", "Occupied", "Vacant", "Occupied",
# "Vacant", "Occupied"
# ]
# Tasks
# 1. Display vacant parking slot numbers.
# 2.Count occupied and vacant slots.
# 3. Allocate the first vacant slot to a new vehicle.
# 4. Calculate parking occupancy percentage.
# 5. Store updated parking information in parking.txt.


parking_slots = [
"Occupied", "Vacant", "Occupied", "Vacant",
"Occupied", "Occupied", "Vacant", "Occupied",
"Vacant", "Occupied"
]


#1.Display vacant parking slot 
print("Vacant slot numbers :")
for i in range(len(parking_slots)):
    if parking_slots[i]=="Vacant":
        print(i)


#2.count occupied and vacant slots.
count_vacant=0
count_occupied=0

for items in parking_slots:
    if items == "Vacant":
        count_vacant+=1

    else:
        count_occupied+=1

print("occupied slots : ",count_occupied)
print("vacant slots : ",count_vacant)


#3.Allocate the first vacant slot to a new vehicle.
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print("Allocated slot number : ",i+1)
        break


#4.Calculate parking occupancy percentage.
total_slots = len(parking_slots)

occupied_slots = 0     #initialisation of occupied slots

for slot in parking_slots:
    if slot == "Occupied":
        occupied_slots += 1

#calculate the occupancy percentage
parking_occupancy_percentage = (occupied_slots / total_slots) * 100

print("Parking occupancy percentage : ",parking_occupancy_percentage)


#5.Store updated parking information in parking.txt.
file = open("classwork/python_coding_challenge-1/parking.txt", "w")
for slot in parking_slots:
    file.write(slot + "\n")
file.close()

