# Problem Statement
# Monthly electricity consumption (units) is stored as:
# units = {
# "House101": 320,
# "House102": 180,
# "House103": 510,
# "House104": 275,
# "House105": 150,
# "House106": 430,
# "House107": 220,
# "House108": 390,
# "House109": 145,
# "House110": 600
# }
# Tasks
# 1. Display houses consuming more than 400 units.
# 2. Find the highest-consuming house.
# 3. Find the lowest-consuming house.
# 4. Calculate total units consumed.
# 5. Create lists:
# o Low Consumption (< 200)
# o Medium Consumption (200–400)
# o High Consumption (> 400)
# 6. Count houses eligible for an energy-saving campaign (consumption > 300).

units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,    
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

#---------------------------------------------------------------
#task 1 : Display houses consuming more than 400 units.
print("Houses consuming more than 400 units:")
for house, consumption in units.items():
    if consumption > 400:
        print(f"{house}: {consumption} units")


#---------------------------------------------------------------

units_list = list(units.items())
#task 2 : Find the highest-consuming house.
highest_consuming_house = units_list[0]
for house in units_list:
    if house[1] > highest_consuming_house[1]:
        highest_consuming_house = house

print(f"\nHighest-consuming house: {highest_consuming_house[0]} ({highest_consuming_house[1]} units)")

#---------------------------------------------------------------
#task 3 : Find the lowest-consuming house.
lowest_consuming_house = units_list[0]
for house in units_list:
    if house[1] < lowest_consuming_house[1]:
        lowest_consuming_house = house

print(f"\nLowest-consuming house: {lowest_consuming_house[0]} ({lowest_consuming_house[1]} units)")

#---------------------------------------------------------------
#task 4 : Calculate total units consumed.
total_units = 0
for consumption in units.values():
    total_units += consumption

print(f"\nTotal units consumed: {total_units} ")

#---------------------------------------------------------------
#task 5 : Create lists:
low_consumption = []
medium_consumption = []
high_consumption = []
for house, consumption in units.items():
    if consumption < 200:
        low_consumption.append(house)
    elif 200 <= consumption <= 400:
        medium_consumption.append(house)
    else:
        high_consumption.append(house)

print(f"\nLow Consumption : {low_consumption}")
print(f"\nMedium Consumption : {medium_consumption}")
print(f"\nHigh Consumption : {high_consumption}")

#---------------------------------------------------------------
#task 6 : Count houses eligible for an energy-saving campaign (consumption > 300).
eligible_houses_count = 0
for consumption in units.values():
    if consumption > 300:
        eligible_houses_count += 1

print(f"\nNumber of houses eligible for energy-saving campaign: {eligible_houses_count}")




'''
output:
Houses consuming more than 400 units:
House103: 510 units
House106: 430 units
House110: 600 units 

Highest-consuming house: House110 (600 units)

Lowest-consuming house: House109 (145 units)

Total units consumed: 3200

Low Consumption : ['House102', 'House105', 'House109']

Medium Consumption : ['House101', 'House104', 'House107', 'House108']

High Consumption : ['House103', 'House106', 'House110']

Number of houses eligible for energy-saving campaign: 6

'''