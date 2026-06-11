# Employee Payroll Management System
# Problem Statement
# A company stores employee details in a text file named employees.txt.
# File Format
# EMP101,Anuj,45000
# EMP102,Rahul,52000
# EMP103,Priya,38000
# EMP104,Neha,61000
# EMP105,Amit,29000
# EMP106,Sneha,55000
# EMP107,Karan,47000
# EMP108,Pooja,72000
# EMP109,Rohit,33000
# EMP110,Anjali,68000
# Requirements
# Create a menu-driven program to:
# 1. Display all employee records.
# 2. Search employee details using Employee ID.
# 3. Calculate the average salary.
# 4. Find the highest-paid and lowest-paid employee.
# 5. Display employees earning above ₹50,000.
# 6. Add a new employee record to the file.
# 7. Generate salary categories:
# o High (₹60,000 and above)
# o Medium (₹40,000–₹59,999)
# o Low (Below ₹40,000)



#---------------------------------------------------------------
# Employee Payroll Management System
#---------------------------------------------------------------
#operation using file handling

#create a file
file = open("Labwork/file_handling_10th-June/employees.txt", "r")

#menu drive for users to select
print("----------Employee Payroll Management System----------")
print("1. Display all employee records.")
print("2. Search employee details using Employee ID.")
print("3. Calculate the average salary.")
print("4. Find the highest-paid and lowest-paid employee.")
print("5. Display employees earning above ₹50,000.")
print("6. Add a new employee record to the file.")
print("7. Generate salary categories.")
print("8. Exit.")




while True:
    choice = int(input("Enter your choice: "))

    #display all employee records
    if choice == 1:
        print("All employee records:")
        for line in file:
            data=line.strip().split(",")
            print("Employee ID:", data[0])
            print("Name:", data[1])
            print("Salary:", data[2])
            print()

    
    #search employee details using Employee ID
    elif choice == 2:
        employee_id = input("Enter Employee ID: ")
        for line in file:
            data=line.strip().split(",")
            if data[0] == employee_id:
                print("Employee ID:", data[0])
                print("Name:", data[1])
                print("Salary:", data[2])
                print()
                break
        else:
            print("Employee not found.")


    #calculate the average salary
    elif choice == 3:
        total_salary = 0
        count = 0
        for line in file:
            data=line.strip().split(",")
            total_salary += float(data[2])
            count += 1
        if count > 0:
            average_salary = total_salary / count
            print("Average salary:", average_salary)
        else:
            print("No employee records found.")


    #find the highest-paid and lowest-paid employee
    elif choice == 4:
        highest_salary = 0
        lowest_salary = float('inf')
        for line in file:
            data=line.strip().split(",")
            salary = float(data[2])
            if salary > highest_salary:
                highest_salary = salary
                highest_employee = data[0]
            if salary < lowest_salary:
                lowest_salary = salary
                lowest_employee = data[0]
        print("Highest-paid employee:", highest_employee)
        print("Lowest-paid employee:", lowest_employee)
        print("Highest salary:", highest_salary)
        print("Lowest salary:", lowest_salary)
    


    #display employees earning above ₹50,000
    elif choice == 5:
        print("Employees earning above ₹50,000:")
        for line in file:
            data=line.strip().split(",")
            if float(data[2]) > 50000:
                print("Employee ID:", data[0])
                print("Name:", data[1])
                print("Salary:", data[2])
                print()


    #add a new employee record to the file
    elif choice == 6:

        file.close()
        file = open("Labwork/file_handling_10th-June/employees.txt", "a")
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")
        file.write(f"{employee_id},{name},{salary}\n")
        print("Employee record added successfully.")
        file.close()
        file = open("Labwork/file_handling_10th-June/employees.txt", "r")


    #generate salary categories
    elif choice == 7:
        print("Salary categories:")
        salary_categories = {}
        high_salary = 0
        medium_salary = 0
        low_salary = 0
        for line in file:
            data=line.strip().split(",")
            salary = float(data[2])
            if salary > 60000:
                high_salary += 1
                if data[0] not in salary_categories:
                    salary_categories[data[0]] = "High"
            elif salary > 40000:
                medium_salary += 1
                if data[0] not in salary_categories:
                    salary_categories[data[0]] = "Medium"
            else:
                low_salary += 1
                if data[0] not in salary_categories:
                    salary_categories[data[0]] = "Low"

        for employee_id, category in salary_categories.items():
            print(f"Employee ID: {employee_id}, Category: {category}")

        print(f"High Salary: {high_salary}")
        print(f"Medium Salary: {medium_salary}")
        print(f"Low Salary: {low_salary}")

    #exit the program
    elif choice == 8:
        print("Exiting the program.")
        file.close()
        break
    
        
