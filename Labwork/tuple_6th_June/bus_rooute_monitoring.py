# ---------------------------------------------------------
# Program: Bus Route Monitoring
# ---------------------------------------------------------

passengers = [12, 18, 25, 30, 28, 15, 8]

# Find busiest stop
max_passengers = max(passengers)
busiest_stop = passengers.index(max_passengers) + 1

# Find stops with fewer than 10 passengers
low_passenger_stops = []

for i in range(len(passengers)):
    if passengers[i] < 10:
        low_passenger_stops.append(i + 1)

# Calculate average passengers
average = sum(passengers) / len(passengers)

# Check if any stop exceeded 25 passengers
exceeded = False

for count in passengers:
    if count > 25:
        exceeded = True
        break

# Display results
print("Busiest Stop:", busiest_stop)
print("Passengers at Busiest Stop:", max_passengers)
print("Stops with fewer than 10 passengers:", low_passenger_stops)
print("Average Passengers:", average)

if exceeded:
    print("At least one stop exceeded 25 passengers.")
else:
    print("No stop exceeded 25 passengers.")