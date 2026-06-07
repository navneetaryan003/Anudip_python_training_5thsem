# ---------------------------------------------------------
# Program: Water Tank Filling Simulation
# Description:
# A tank starts with 0 liters of water.
# Water is added at a constant rate every minute.
# The program displays the water level after each minute
# until the tank reaches its maximum capacity.
# ---------------------------------------------------------

# Tank configuration
tank_capacity = 100      # Maximum capacity of tank (liters)
water_level = 0          # Initial water level (liters)
fill_rate = 10           # Water added per minute (liters)

# -------------------------
# Validation Section
# -------------------------

# Capacity must be positive
if tank_capacity <= 0:
    print("Error: Tank capacity must be greater than 0.")

# Fill rate must be positive
elif fill_rate <= 0:
    print("Error: Fill rate must be greater than 0.")

# Initial water level cannot be negative
elif water_level < 0:
    print("Error: Initial water level cannot be negative.")

# Initial water level cannot exceed capacity
elif water_level > tank_capacity:
    print("Error: Initial water level cannot exceed tank capacity.")

else:
    print("Tank Filling Process Started...\n")

    minute = 0

    # Continue filling until tank becomes full
    while water_level < tank_capacity:

        minute += 1

        # Add water
        water_level += fill_rate

        # Prevent overflow
        if water_level > tank_capacity:
            water_level = tank_capacity

        print(f"Minute {minute}: Water Level = {water_level} liters")

    print("\nTank is full.")