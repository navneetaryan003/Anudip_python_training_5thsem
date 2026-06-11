# Movie Ticket Booking System
# Problem Statement
# Seat booking status in a cinema hall is stored as follows.
# Sample Data
# tickets = {
# "A1": "Booked",
# "A2": "Available",
# "A3": "Booked",
# "A4": "Available",
# "B1": "Booked",
# "B2": "Available",
# "B3": "Booked",
# "B4": "Available",
# "C1": "Booked",
# "C2": "Available"
# }
# Tasks
# 1. Display available seats.
# 2. Count booked and available seats.
# 3. Reserve the first available seat.
# 4. Save updated booking details to tickets.txt.
# 5. Calculate hall occupancy percentage.



tickets = {
"A1": "Booked",
"A2": "Available",
"A3": "Booked",
"A4": "Available",
"B1": "Booked",
"B2": "Available",
"B3": "Booked",
"B4": "Available",
"C1": "Booked",
"C2": "Available"
}


#1. Display available seats
print("Available seats:")
for seat, status in tickets.items():
    if status == "Available":
        print(seat)


#2. Count booked and available seats
booked_seats = 0     #initialisation of booked seats
available_seats = 0   # initialisation of available seats

for seat, status in tickets.items():
    if status == "Booked":
        booked_seats += 1
    else:
        available_seats += 1

print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)


#3. Reserve the first available seat
for seat, status in tickets.items():
    if status == "Available":
        tickets[seat] = "Booked"
        print(f"Seat {seat} reserved successfully.")
        break


#4. Save updated booking details to tickets.txt
file= open("classwork/python_coding_challenge-1/tickets.txt", "w")
for seat, status in tickets.items():
        file.write(seat + ": " + status + "\n")

file.close()


#5. Calculate hall occupancy percentage
occupied_seats = 0

for seat, status in tickets.items():
    if status == "Booked":
        occupied_seats += 1

occupancy_percentage = (occupied_seats / len(tickets)) * 100
print(f"Occupancy Percentage: {occupancy_percentage:.2f}%")