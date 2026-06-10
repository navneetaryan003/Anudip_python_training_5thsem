# Railway Reservation Seat Analyzer
# Problem Statement
# A railway coach has seats represented as follows:
# seats = [
# "Booked", "Available", "Booked", "Booked",
# "Available", "Available", "Booked", "Available",
# "Booked", "Booked", "Available", "Booked"
# ]
# Requirements
# Create the following functions:
# 1. count_seats(seats)
# Returns the number of booked and available seats.
# 2. first_available(seats)
# Returns the seat number of the first available seat.
# 3. occupancy_percentage(seats)
# Returns the percentage of occupied seats.
# 4. display_available_seats(seats)
# Displays all available seat numbers.

# Railway Reservation Seat Analyzer

seats = [
"Booked", "Available", "Booked", "Booked",
"Available", "Available", "Booked", "Available",
"Booked", "Booked", "Available", "Booked"
]


# Function to count booked and available seats
def count_seats(seats):
    booked = 0
    available = 0
    for seat in seats:
        if seat == "Booked":
            booked += 1
        else:
            available += 1
    return booked, available

# Function to find the first available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return  i + 1
    return None

# Function to calculate the occupancy percentage
def occupancy_percentage(seats):
    total_seats = len(seats)
    occupied_seats = 0
    for seat in seats:
        if seat == "Booked":
            occupied_seats += 1
    return (occupied_seats / total_seats) * 100

# Function to display available seats
def display_available_seats(seats):
    available_list=[]
    for i in range(len(seats)):
        if seats[i] == "Available":
            available_list.append(i+1)
    return available_list   



# Main program

# Call the function for counting booked and available seats
booked, available = count_seats(seats)
print("Booked Seats:", booked)
print("Available Seats:", available)

# Call the function for finding the first available seat
print("First Available Seat:", first_available(seats))

# Call the function for calculating the occupancy percentage
print(f"Occupancy Percentage: {occupancy_percentage(seats):.2f}%")

# Call the function for displaying available seats
available_seats = display_available_seats(seats)
print("Available Seats:")
for seat in available_seats:
    print(seat)