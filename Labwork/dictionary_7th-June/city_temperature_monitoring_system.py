# Problem Statement
# Daily temperatures of different cities are stored as:
# temperature = {
# "Delhi": 41,
# "Mumbai": 33,
# "Chennai": 37,
# "Kolkata": 39,
# "Bengaluru": 28,
# "Pune": 30,
# "Jaipur": 42,
# "Lucknow": 40,
# "Hyderabad": 35,
# "Ahmedabad": 43
# }
# Tasks
# 1. Display cities having temperature above 40°C.
# 2. Find the hottest city.
# 3. Find the coolest city.
# 4. Calculate average temperature.
# 5. Create a list of pleasant cities (temperature < 35°C).
# 6. Count cities with temperature between 35°C and 40°C.

#------------------------------------------------
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

#-----------------------------------------------
#task 1 : Display cities having temperature above 40°C.
print("Cities with temperature above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

#-----------------------------------------------
#task 2 : Find the hottest city.
temperature_list = list(temperature.items())
hottest_city = temperature_list[0]
for city, temp in temperature_list:
    if temp > hottest_city[1]:
        hottest_city = (city, temp)

print(f"Hottest city: {hottest_city[0]}  ({hottest_city[1]}°C)")

#-----------------------------------------------
#task 3 : Find the coolest city.
coolest_city = temperature_list[0]
for city, temp in temperature_list:
    if temp < coolest_city[1]:
        coolest_city = (city, temp) 

print(f"Coolest city: {coolest_city[0]}  ({coolest_city[1]}°C)")

#-----------------------------------------------
#task 4 : Calculate average temperature.
total_temp = 0
for temp in temperature.values():
    total_temp += temp

average_temp = total_temp / len(temperature)
print(f"Average temperature: {average_temp:.2f}°C")

#-----------------------------------------------
#task 5 : Create a list of pleasant cities (temperature < 35°C).
pleasant_cities = []
for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print("Pleasant cities (temperature < 35°C):")
print(pleasant_cities)

#-----------------------------------------------
#task 6 : Count cities with temperature between 35°C and 40°C.
count_cities = 0
for temp in temperature.values():
    if 35 <= temp <= 40:
        count_cities += 1

print(f"Number of cities with temperature between 35°C and 40°C: {count_cities}")


'''
output:
Cities with temperature above 40°C:
Delhi
Jaipur
Ahmedabad

Hottest city: Ahmedabad  (43°C)
Coolest city: Bengaluru  (28°C)

Average temperature: 36.80°C

Pleasant cities (temperature < 35°C):
['Mumbai', 'Bengaluru', 'Pune']

Number of cities with temperature between 35°C and 40°C: 4

'''