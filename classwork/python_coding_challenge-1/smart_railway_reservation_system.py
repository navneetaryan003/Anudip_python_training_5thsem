#  Smart Railway Reservation System
# Problem Statement
# A railway reservation system stores the booking status of seats in a train coach.
# Sample Data
# seats = {
# 1: "Booked",
# 2: "Available",
# 3: "Booked",
# 4: "Available",
# 5: "Booked",
# 6: "Booked",
# 7: "Available",
# 8: "Booked",
# 9: "Available",
# 10: "Booked"
# }
# Tasks
# 1. Display all available seat numbers.
# 2. Count booked and available seats.
# 3. Reserve the first available seat.
# 4. Cancel booking for a given seat number.
# 5. Store the updated reservation status in reservations.txt.
# 6. Display occupancy percentage.

seats = {
1: "Booked",
2: "Available",
3: "Booked",
4: "Available",
5: "Booked",
6: "Booked",
7: "Available",
8: "Booked",
9: "Available",
10: "Booked"
}


#1. Display all available seat numbers
print("Available Seats:")
for seat, status in seats.items():
    if status == "Available":
        print(seat)


#2. Count booked and available seats
booked_seats = 0     #counting the number of booked seats
available_seats = 0     #counting the number of available seats

for status in seats.values():

    #counting the number of booked and available seats
    if status == "Booked":
        booked_seats += 1
    elif status == "Available":
        available_seats += 1
       
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)


#3. Reserve the first available seat
for seat, status in seats.items():
    if status == "Available":
        seats[seat] = "Booked"
        print(f"Seat {seat} reserved successfully.")
        break

#4. Cancel booking for a given seat number
seat_to_cancel = int(input("Enter the seat number to cancel: "))
if seat_to_cancel in seats:
    seats[seat_to_cancel] = "Available"


#5. Store the updated reservation status in reservations.txt
file= open("classwork/python_coding_challenge-1/reservations.txt", "w")
for seat, status in seats.items():
        file.write(f"Seat {seat}: {status}\n")

file.close()


#6. Display occupancy percentage
occupied_seats = 0
for seat, status in seats.items():
    if status == "Booked":
        occupied_seats += 1
occupancy_percentage = (occupied_seats / len(seats)) * 100
print(f"Occupancy Percentage: {occupancy_percentage:.2f}%")



   
