# City Population & Development Dashboard
# Problem Statement
# The government wants to analyze city data.
# Store details of at least 30 cities.
# Example Structure
# cities = {
# "Delhi": {
# "population": 32000000,
# "area": 1484,
# "literacy": 89
# }
# }
# Requirements
# 1. Display all city details.
# 2. Find the most populated city.
# 3. Find the least populated city.
# 4. Calculate average population.
# 5. Display cities with literacy rate above 90%.
# 6. Display cities with literacy below average.
# 7. Calculate population density.
# 8. Find city with highest density.
# 9. Categorize cities:
# o Small
# o Medium
# o Large
# 10. Create a development-priority list.
# 11. Generate separate dictionaries for:
# o High Literacy Cities
# o Low Literacy Cities
# 12. Generate a national summary report.
# Challenge
# Rank all cities based on population density.


n=30   #minimum number of cities

cities={}   #empty dictionary

while True:

    #input name of the city
    city_name=input("Enter city name:")

    #validate city name if it already exists
    if city_name in cities:
        print("City name already exists. Please enter a unique name.")
        continue

    #validate city name
    if not city_name.replace(" ","").isalpha():
        print("Invalid city name. Please enter a valid name.")
        continue

    #input population, area and literacy
    population=int(input("Enter population:"))

    #validate population
    if population < 0:
        print("Invalid population. Please enter a valid population.")
        continue

    area=int(input("Enter area:"))

    #validate area
    if area <= 0:
        print("Invalid area. Please enter a valid area.")
        continue


    literacy=float(input("Enter literacy rate:"))

    #validate literacy
    if literacy < 0 or literacy > 100:
        print("Invalid literacy rate. Please enter a valid literacy rate.")
        continue
    

    #store details in dictionary
    cities[city_name]={
        "population":population,
        "area":area,
        "literacy":literacy
    }

    #validating the minimum number of cities

    if len(cities)<n:
        continue

    else: 

        #ask user to continue or exit
        choice = input("Do you want to continue? (yes/no) : ")
        if choice.lower() != "yes":
            break


# 1. Display all city details.
print("All city details:")
for city, details in cities.items():
    print(f"City: {city}")
    print(f"Population: {details['population']}")
    print(f"Area: {details['area']}")
    print(f"Literacy: {details['literacy']}")
    print('-----'*2)

print('-----'*5)


# 2. Find the most populated city.
most_populated_city = (list(cities.keys()))[0]
most_populated_city_population = cities[most_populated_city]["population"]
for city_name, details in cities.items():
    if details["population"] > cities[most_populated_city]["population"]:
        most_populated_city = city_name
        most_populated_city_population = details["population"]

print(f"Most populated city: {most_populated_city} with {most_populated_city_population} population")
print('-----'*5)

# 3. Find the least populated city.
least_populated_city = (list(cities.keys()))[0]
least_populated_city_population = cities[least_populated_city]["population"]
for city_name, details in cities.items():
    if details["population"] < cities[least_populated_city]["population"]:
        least_populated_city = city_name
        least_populated_city_population = details["population"]

print(f"Least populated city: {least_populated_city} with {least_populated_city_population} population")
print('-----'*5)

# 4. Calculate average population.
total_population = 0
for city_name, details in cities.items():
    total_population += details["population"]

average_population = total_population / len(cities)

print(f"Average population: {average_population}")
print('-----'*5)

# 5. Display cities with literacy rate above 90%.
for city_name, details in cities.items():
    if details["literacy"] > 90:
        print(f"City: {city_name}")
        print(f"Literacy: {details['literacy']}")
        print('-----'*2)

print('-----'*5)


# 6. Display cities with literacy below average.
# calculate average literacy
total_literacy = 0
for city_name, details in cities.items():
    total_literacy += details["literacy"]

average_literacy = total_literacy / len(cities)

for city_name, details in cities.items():
    if details["literacy"] < average_literacy:
        print(f"City: {city_name}")
        print(f"Literacy: {details['literacy']}")
        print('-----'*2)

print('-----'*5)

# 7. Calculate population density.
density_stored={}

for city_name, details in cities.items():
    density=details["population"]/details["area"]
    density_stored[city_name]=density

print("Population Density:")
for city_name, density in density_stored.items():
    print(f"City: {city_name}")
    print(f"Population Density: {density}")
    print('-----'*2)

print('-----'*5)


# 8. Find city with highest density.

highest_density_city = (list(density_stored.keys()))[0]
highest_density = density_stored[highest_density_city]
for city_name, density in density_stored.items():
    if density > highest_density:
        highest_density_city = city_name
        highest_density = density

print(f"Highest density city: {highest_density_city} with {highest_density} population density")
print('-----'*5)

# 9. Categorize cities:
# o Small
# o Medium
# o Large

print("City Categories:")
for city_name, details in cities.items():
    #small
    if details["population"] < average_population:
        print(f"City: {city_name}")
        print("Category: Small")
        print('-----'*5)

    #large    
    elif details["population"] > average_population:
        print(f"City: {city_name}")
        print("Category: Large")
        print('-----'*5)

    #medium    
    else:
        print(f"City: {city_name}")
        print("Category: Medium")
        print('-----'*2)

print('-----'*5)


# 10. Create a development-priority list.

development_priority_list = {}

for city_name, details in cities.items():
    if details["literacy"] < average_literacy:
        development_priority_list[city_name] = details

print("Development Priority List:")
for city_name,details in development_priority_list.items():
    print(f"City: {city_name}")
    print(f"Population: {details['population']}")
    print(f"Area: {details['area']}")
    print(f"Literacy: {details['literacy']}")
    print('-----'*2)

print('-----'*5)


# 11. Generate separate dictionaries for:
# o High Literacy Cities
# o Low Literacy Cities

high_literacy_cities = {}
low_literacy_cities = {}

for city_name, details in cities.items():
    if details["literacy"] > average_literacy:
        high_literacy_cities[city_name] = details
    else:
        low_literacy_cities[city_name] = details

print("High Literacy Cities:")
for city_name, details in high_literacy_cities.items():
    print(f"City: {city_name}")
    print(f"Population: {details['population']}")
    print(f"Area: {details['area']}")
    print(f"Literacy: {details['literacy']}")
    print('-----'*2)

print('-----'*5)

print("Low Literacy Cities:")
for city_name, details in low_literacy_cities.items():
    print(f"City: {city_name}")
    print(f"Population: {details['population']}")
    print(f"Area: {details['area']}")
    print(f"Literacy: {details['literacy']}")
    print('-----'*2)

print('-----'*5)

# 12. Generate a national summary report.

print("National Summary Report:")
#12.1 : total number of cities
print(f"Total number of cities: {len(cities)}")

#12.2 : average literacy rate
print(f"Average literacy rate: {average_literacy}")

#12.3 : average population
print(f"Average population: {average_population}")

# 12.4: Find the most populated city.
most_populated_city = (list(cities.keys()))[0]
most_populated_city_population = cities[most_populated_city]["population"]
for city_name, details in cities.items():
    if details["population"] > cities[most_populated_city]["population"]:
        most_populated_city = city_name
        most_populated_city_population = details["population"]

print(f"Most populated city: {most_populated_city} with {most_populated_city_population} population")


# 12.5: Find the least populated city.

least_populated_city = (list(cities.keys()))[0]
least_populated_city_population = cities[least_populated_city]["population"]
for city_name, details in cities.items():
    if details["population"] < cities[least_populated_city]["population"]:
        least_populated_city = city_name
        least_populated_city_population = details["population"]

print(f"Least populated city: {least_populated_city} with {least_populated_city_population} population")

#12.6 : most literacy city
most_literacy_city = (list(cities.keys()))[0]
most_literacy = cities[most_literacy_city]["literacy"]
for city_name, details in cities.items():
    if details["literacy"] > cities[most_literacy_city]["literacy"]:
        most_literacy_city = city_name
        most_literacy = details["literacy"]

print(f"Most literacy city: {most_literacy_city} with {most_literacy} literacy")

#12.7 : least literacy city
least_literacy_city = (list(cities.keys()))[0]
least_literacy = cities[least_literacy_city]["literacy"]
for city_name, details in cities.items():
    if details["literacy"] < cities[least_literacy_city]["literacy"]:
        least_literacy_city = city_name
        least_literacy = details["literacy"]

print(f"Least literacy city: {least_literacy_city} with {least_literacy} literacy")

print('-----'*5)


# Challenge
# Rank all cities based on population density.
for city_name, details in cities.items():

    if details["population"] > average_population:

        print(f"City: {city_name}")
        print(f"Population: {details['population']}")
        print("Category: Large")

    elif details["population"] < average_population:

        print(f"City: {city_name}")
        print(f"Population: {details['population']}")
        print("Category: Small")

    else:

        print(f"City: {city_name}")
        print(f"Population: {details['population']}")
        print("Category: Medium")

print('-----'*5)