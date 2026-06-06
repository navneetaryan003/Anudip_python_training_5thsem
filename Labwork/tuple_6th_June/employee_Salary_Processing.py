# Write a program to:
# • Display employees earning above ₹50,000.
# • Find the highest-paid employee.
# • Calculate total salary expenditure.
# • Count employees earning below ₹40,000.

#employees details with their salary 

employees = [
("Rahul", 35000),
("Priya", 55000),
("Amit", 42000),
("Neha", 65000)
]

highest=employees[0]     #intialisation of highest salary


sum=0      #for calculating the total salary expenditure

count=0        #for counting whose salary is less than 40000

for emp in employees:

    #task 1 : Display employees earning above ₹50,000.

    if emp[1]>50000:
        print(emp)

    #task 2 : Find the highest-paid employee.
    if emp[1]>highest[1]:
        highest=emp
       
    #task 3: Calculate total salary expenditure.
    sum+=emp[1]


    #task 4 :Count employees earning below ₹40,000. 
    if emp[1]<40000:
        count+=1

print("Highest paid employee :",highest[0])

print("Total salary expenditure :",sum)

print("number of employees whose salary is below Rs40000 :",count)
    

