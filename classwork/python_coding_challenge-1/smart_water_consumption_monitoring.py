# Smart Water Consumption Monitoring System
# Problem Statement
# Monthly water consumption (in litres) of households is recorded below.
# Sample Data
# water_usage = {
# "House101": 1800,
# "House102": 2200,
# "House103": 3500,
# "House104": 2800,
# "House105": 1600,
# "House106": 4100,
# "House107": 2400,
# "House108": 3900,
# "House109": 1500,
# "House110": 4500
# }
# Tasks
# 1. Display houses consuming more than 3000 litres.
# 2. Find the highest and lowest consumers.
# 3. Calculate total water consumption.
# 4. Categorize houses:
# o Low (<2000 litres)
# o Medium (2000–3500 litres)
# o High (>3500 litres)
# 5. Count households eligible for conservation awareness programs (>2500 litres).


water_usage = {
"House101": 1800,
"House102": 2200,
"House103": 3500,
"House104": 2800,
"House105": 1600,
"House106": 4100,
"House107": 2400,
"House108": 3900,
"House109": 1500,
"House110": 4500
}


# 1. Display houses consuming more than 3000 litres.
print("Houses consuming more than 3000 litres:")
for house, usage in water_usage.items():
    if usage > 3000:
        print(f"{house}: {usage} litres")


#2. Find the highest and lowest consumers.
lowest_consumer = min(water_usage, key=water_usage.get)
highest_consumer = max(water_usage, key=water_usage.get)
print(f"Lowest Consumer: {lowest_consumer}")
print(f"Highest Consumer: {highest_consumer}")


#3. Calculate total water consumption.
total_consumption = sum(water_usage.values())
print(f"Total Water Consumption: {total_consumption} litres")


#4. Categorize houses:
# o Low (<2000 litres)
# o Medium (2000–3500 litres)
# o High (>3500 litres)

low_consume=[]
medium_consume=[]
high_consume=[]

category = {}

for house, usage in water_usage.items():
    if usage < 2000:
        low_consume.append(house)

    elif 2000 <= usage <= 3500:
        medium_consume.append(house)

    else:
        high_consume.append(house)

print("Low Consumption Houses:", low_consume)
print("Medium Consumption Houses:", medium_consume)
print("High Consumption Houses:", high_consume)

    

#5. Count households eligible for conservation awareness programs (>2500 litres).
conservation_awareness_count = 0

for usage in water_usage.values():
    if usage > 2500:
        conservation_awareness_count += 1

print(f"Number of households eligible for conservation awareness programs: {conservation_awareness_count}")