# Write a Python program to:
# 1. Display details of employees scoring 80 or above.
# 2. Count the number of employees who need improvement (score below 60).
# 3. Find the employee with the highest score.
# 4. Create a list containing the names of all employees scoring above 75.
# 5. Display the performance category for each employee:
# o 90 and above → Excellent
# o 75 to 89 → Good
# o 60 to 74 → Average
# o Below 60 → Needs Improvement


#employees details in a company
employees = (
("E101", "Anuj", 92),
("E102", "Rahul", 76),
("E103", "Priya", 58),
("E104", "Neha", 98),
("E105", "Amit", 45)
)

highest_score=employees[0][2]
count=0
employees_list=[]

print("Employees scoring 80 or above : ")
for record in employees:

    #task1: To display details of employees scoring 80 or above.
    if record[2]>80:
        print(record)

    #task2:To Count the number of employees who need improvement (score below 60).
    if record[2]<60:
       count+=1

    #task3:to Find the employee with the highest score.
    if(record[2]>highest_score):
        highest_score=record[2]
        top_scorer=record
    
    #task4:To Create a list containing the names of all employees scoring above 75.
    if record[2]>75:
        employees_list.append(record[1])

print("-------------------------------------------")
    
print("Employees needing improvements:",count)

print("-------------------------------------------")

print("Highest Performer :",top_scorer)

print("-------------------------------------------")

print("High Performer :",employees_list)

print("-------------------------------------------")

#task 5. To Display the performance category for each employee:
#  90 and above → Excellent
#  75 to 89 → Good
#  60 to 74 → Average
#  Below 60 → Needs Improvement

for record in employees:
    if record[2]>=90:
        print(record[1],"-> Excellent")
    
    elif record[2]>=75:
        print(record[1],"-> Good")

    elif record[2]>=60:
        print(record[1],"-> Average")
    
    else:
        print(record[1],"-> Needs Improvement")





