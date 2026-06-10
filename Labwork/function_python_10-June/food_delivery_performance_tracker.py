# Food Delivery Performance Tracker
# Problem Statement
# Delivery times (in minutes) for different orders are given below:
# delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]
# Requirements
# Create the following functions:
# 1. fastest_delivery(times)
# Returns the shortest delivery time.
# 2. delayed_orders(times)
# Returns a list of orders taking more than 45 minutes.
# 3. average_delivery_time(times)
# Returns the average delivery time.
# 4. delivery_category(times)
# Displays order categories:
# • Fast → ≤ 30 minutes
# • Normal → 31–45 minutes
# • Delayed → > 45 minutes

# Food Delivery Performance Tracker

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]


# Function to find the fastest delivery time
def fastest_delivery(times):
    min_time = times[0]
    for time in times:
        if time <= min_time:
            min_time = time
    return min_time


# Function to find orders taking more than 45 minutes
def delayed_orders(times):
    delayed = []
    for time in times:
        if time > 45:
            delayed.append(time)
    return delayed


# Function to calculate the average delivery time
def average_delivery_time(times):
    total_time = 0
    for time in times:
        total_time += time
    return total_time / len(times)  

# Function to display order categories
def delivery_category(times):

    # Create a dictionary to store order categories
    order_category = {}

    for time in times:

        
        if time <= 30:

            # Check if the order category has already been assigned
            if time not in order_category:
                  order_category[time] = "Fast"


        elif time <= 45:

            # Check if the order category has already been assigned
            if time not in order_category:
                  order_category[time] = "Normal"
          
        else:
            
            # Check if the order category has already been assigned
            if time not in order_category:
                  order_category[time] = "Delayed"
    return order_category


#Main program

#print the fastest delivery time
print("Fastest Delivery Time:", fastest_delivery(delivery_time))

#print the orders taking more than 45 minutes
print("Delayed Orders:", delayed_orders(delivery_time))

#print the average delivery time
print("Average Delivery Time:", average_delivery_time(delivery_time))

#print the order categories
category=delivery_category(delivery_time)

#validate the order categories
if category:
    print("Order Categories:")
    for time, category in category.items():
        print(f"Time: {time}, Category: {category}")
else:
    print("No orders found.")