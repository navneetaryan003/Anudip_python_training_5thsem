# Student Performance Analytics System
# Problem Statement
# A coaching institute wants to analyze student performance.
# Store details of at least 30 students in a dictionary.
# Example Structure
# students = {
# "S101": {"name": "Anuj", "marks": 85},
# "S102": {"name": "Rahul", "marks": 72}
# }
# Requirements
# 1. Display all student records.
# 2. Search a student using Student ID.
# 3. Add a new student.
# 4. Update marks of an existing student.
# 5. Delete a student.
# 6. Find topper and lowest scorer.
# 7. Calculate class average.
# 8. Count pass and fail students.
# 9. Generate grades:
# o A (90+)
# o B (75–89)
# o C (50–74)
# o F (<50)
# 10. Display students scoring above average.
# 11. Display top 5 performers.
# 12. Create a separate dictionary for scholarship students (marks > 85).

#empty dictionary to store student records
students = {}


while True:
    student_id = input("Enter student ID : ")
    
    #validate student ID
    #check if student ID already exists
    if student_id in students:
        print(f"Student with ID {student_id} is already present in records")
        continue

    #check if student ID is alphanumeric
    elif not student_id.isalnum():
        print("Invalid student ID. Please enter a valid ID.")
        continue


    name =input("Enter student name : ")

    #validate student name
    #check if student name is alphabetic
    if not name.isalpha():
        print("Invalid student name. Please enter a valid name.")
        continue

    marks = int(input("Enter student marks : "))

    #validate student marks
    
    #check if student marks is between 0 and 100
    if marks < 0 or marks > 100 :
        print("Invalid student marks. Please enter a valid marks.")
        continue
    
    #add student record to dictionary
    students[student_id] = {
        "name": name,
        "marks": marks
    }
    
    #ask user if they want to add another student
    choice = input("Do you want to add another student? (yes/no) : ")
    if choice.lower() != "yes":
        break

#1.display student records
print("Student Records : ")
for student_id, student_info in students.items():
    print(f"ID: {student_id}, Name: {student_info['name']}, Marks: {student_info['marks']}")

#2.search student using student ID
student_id_search=input("Enter student ID to search : ")
if student_id_search in students:
    student_info = students[student_id_search]
    print(f"Name: {student_info['name']}, Marks: {student_info['marks']}")
else:
    print(f"Student with ID {student_id_search} not found.")


#3.add student 
new_student_id=input("enter the new student id :")
if new_student_id in students:
    print(f"Student with student id {new_student_id} is already present in records")

else:
    name=input("enter the name :")
    marks=int(input("enter the marks :"))
    students[new_student_id] = {
        "name": name,
        "marks": marks
    }

print("New student record added successfully") 

#4.update marks
student_id_update=input("Enter student ID to update marks : ")
if student_id_update in students:
    new_marks = int(input("Enter new marks : "))
    students[student_id_update]["marks"] = new_marks
    print(f"Marks for student with ID {student_id_update} updated successfully.")
else:
    print(f"Student with ID {student_id_update} not found.")


#5.delete student
student_id_delete=input("Enter student ID to delete : ")
if student_id_delete in students:
    del students[student_id_delete]
    print(f"Student with ID {student_id_delete} deleted successfully.")
else:
    print(f"Student with ID {student_id_delete} not found.")


#6.find topper and lowest scorer
topper = students[0]
lowest_scorer = students[0]

for student_id, student_info in students.items():
    if student_info["marks"] > topper["marks"]:
        topper = student_info
    if student_info["marks"] < lowest_scorer["marks"]:
        lowest_scorer = student_info

print(f"topper id : {topper['id']}, name : {topper['name']}, marks : {topper['marks']}")
print(f"lowest scorer id : {lowest_scorer['id']}, name : {lowest_scorer['name']}, marks : {lowest_scorer['marks']}")


#7.calculate class average
total_marks = 0
for student_id, student_info in students.items():
    total_marks += student_info["marks"]

class_average = total_marks / len(students)
print(f"Class average : {class_average}")

#8.count pass and fail students
pass_count = 0
fail_count = 0
for student_id, student_info in students.items():
    if student_info["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1

print(f"Pass count : {pass_count}")
print(f"Fail count : {fail_count}")

#9.generate grades
for student_id, student_info in students.items():
    if student_info["marks"] >= 90:
        grade = "A"
    elif student_info["marks"] >= 75:
        grade = "B"
    elif student_info["marks"] >= 50:
        grade = "C"
    else:
        grade = "F"
    print(f"ID: {student_id}, Name: {student_info['name']}, Marks: {student_info['marks']}, Grade: {grade}")


#10.display students scoring above average
for student_id, student_info in students.items():
    if student_info["marks"] > class_average:
        print(f"ID: {student_id}, Name: {student_info['name']}, Marks: {student_info['marks']}")


#11.display top 5 performers
sorted_students = sorted(students.items(), key=lambda student_id: student_id[1]["marks"], reverse=True)
top_5 = sorted_students[:5]

for student_id, student_info in top_5:
    print(f"ID: {student_id}, Name: {student_info['name']}, Marks: {student_info['marks']}")



#12.create a seperate dictionary for scholarship students
scholarship_students = {}
for student_id, student_info in students.items():
    if student_info["marks"] > 85:
        scholarship_students[student_id] = student_info

print("Scholarship Students:" , scholarship_students)

    