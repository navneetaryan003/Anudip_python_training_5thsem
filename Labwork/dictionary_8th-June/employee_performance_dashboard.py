# Problem Statement
# Employee performance scores are stored as:
# performance = {
# "EMP101": 92,
# "EMP102": 78,
# "EMP103": 45,
# "EMP104": 88,
# "EMP105": 97,
# "EMP106": 56,
# "EMP107": 81,
# "EMP108": 64,
# "EMP109": 39,
# "EMP110": 73
# }
# Tasks
# 1. Display employees scoring above 80.
# 2. Count employees needing improvement (score < 60).
# 3. Find the top performer.
# 4. Calculate average performance score.
# 5. Create separate lists:
# o Excellent (≥ 90)
# o Good (75–89)
# o Average (60–74)
# o Poor (< 60)


#-----------------------------------------

performance = {
"EMP101": 92,
"EMP102": 78,          
"EMP103": 45,
"EMP104": 88,
"EMP105": 97,
"EMP106": 56,
"EMP107": 81,
"EMP108": 64,   
"EMP109": 39,
"EMP110": 73
}

#-----------------------------------------
#task 1: display employees scoring above 80
print("Employees scoring above 80:")
for emp_id, score in performance.items():
    if score > 80:
        print(emp_id)

#-----------------------------------------
#task 2: count employees needing improvement (score < 60)
improvement_count = 0
for score in performance.values():
    if score < 60:
        improvement_count += 1

print(f"\nNumber of employees needing improvement: {improvement_count}")

#-----------------------------------------
#task 3: find the top performer
performance_items = list(performance.items())
top_performer = performance_items[0]
for emp_id, score in performance_items:
    if score > top_performer[1]:
        top_performer = (emp_id, score) 

print(f"\nTop performer: {top_performer[0]}  ({top_performer[1]})")

#-----------------------------------------
#task 4: calculate average performance score
total_score = 0
for score in performance.values():
    total_score += score

average_score = total_score / len(performance)
print(f"\nAverage score: {average_score:.2f}")

#-----------------------------------------
#task 5: create separate lists for performance categories
excellent_employees = []    
good_employees = []
average_employees = []
poor_employees = []
for emp_id, score in performance.items():
    if score >= 90:
        excellent_employees.append(emp_id)
    elif 75 <= score < 90:
        good_employees.append(emp_id)
    elif 60 <= score < 75:
        average_employees.append(emp_id)
    else:
        poor_employees.append(emp_id)

print(f"\nExcellent : {excellent_employees}")
print(f"Good : {good_employees}")
print(f"Average : {average_employees}")
print(f"Poor : {poor_employees}")




'''
Output:
Employees scoring above 80:
EMP101
EMP104
EMP105

Number of employees needing improvement: 3
Top performer: EMP105  (97)
Average score: 71.30
Excellent : ['EMP101', 'EMP105']
Good : ['EMP104', 'EMP107']
Average : ['EMP102', 'EMP108', 'EMP110']
Poor : ['EMP103', 'EMP106', 'EMP109']

'''