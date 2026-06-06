#write a program to create a dictionary that contains the record of 10 employees where employee id used as i key and salary is used as a value . find out the total number of employees having salary greater than 30000
#display the list of employees whose salary is below 20000 

salary_record={}

list_employees=[]
for i in range(10):
    employee_id=input("enter the id :")
    salary=int(input("enter the salary :"))
    salary_record[employee_id]=salary

for employee_id,salary in salary_record.items():
    if salary > 30000:
        print(employee_id," : ",salary)
    
    if salary<20000:
        list_employees.append(employee_id)

print(list_employees)