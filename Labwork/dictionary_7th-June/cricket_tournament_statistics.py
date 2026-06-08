# Problem Statement
# Runs scored by players in a tournament:
# runs = {
# "Virat": 645,
# "Rohit": 512,
# "Gill": 698,
# "Rahul": 435,
# "Hardik": 278,
# "Pant": 534,
# "Surya": 389,
# "Jadeja": 301,
# "Iyer": 455,
# "KL": 410
# }
# Tasks
# 1. Display players scoring more than 500 runs.
# 2. Find the Orange Cap winner.
# 3. Find the lowest scorer.
# 4. Calculate total runs scored.
# 5. Create a list of players scoring below 400.
# 6. Count players scoring between 400 and 600 runs.

runs = {
    "Virat": 645,
    "Rohit": 512,          
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,   
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

#-------------------------------------------------------------
# task 1. Display players scoring more than 500 runs.
print("Players scoring more than 500 runs:")
for player, score in runs.items():
    if score > 500:
        print(player)

#-------------------------------------------------------------
# task 2. Find the Orange Cap winner.o
runs_list = list(runs.items())
orange_cap_winner = runs_list[0][0]
for player, score in runs_list:
    if score > runs[orange_cap_winner]:
        orange_cap_winner = player

print(f"\nOrange Cap winner: {orange_cap_winner} ({runs[orange_cap_winner]})")

#-------------------------------------------------------------
# task 3. Find the lowest scorer.
lowest_scorer = runs_list[0][0]
for player, score in runs_list:
    if score < runs[lowest_scorer]:
        lowest_scorer = player

print(f"\nLowest scorer: {lowest_scorer} ({runs[lowest_scorer]})")

#-------------------------------------------------------------
# task 4. Calculate total runs scored.
total_runs=0
for score in runs.values():
    total_runs += score

print("\nTotal runs scored:", total_runs)

#-------------------------------------------------------------
# task 5. Create a list of players scoring below 400.
players_below_400 = []
for player, score in runs.items():
    if score < 400:
        players_below_400.append(player)

print("\nPlayers scoring below 400 runs:", players_below_400)

#-------------------------------------------------------------
# task 6. Count players scoring between 400 and 600 runs.
count_between_400_and_600 = 0
for score in runs.values():
    if 400 <= score <= 600:
        count_between_400_and_600 += 1

print("\nNumber of players scoring between 400 and 600 runs:", count_between_400_and_600)

'''
output:
Players scoring more than 500 runs:
Virat
Rohit
Gill    

Orange Cap winner: Gill
Lowest scorer: Hardik

Total runs scored: 4757

Players scoring below 400 runs: ['Hardik', 'Surya', 'Jadeja']

Number of players scoring between 400 and 600 runs: 5

'''