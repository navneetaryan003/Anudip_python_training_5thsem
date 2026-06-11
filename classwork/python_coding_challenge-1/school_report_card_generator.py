# School Report Card Generator
# Problem Statement
# Student marks are stored in marks.txt.
# Sample Input/Data (marks.txt)
# S101,Anuj,92
# S102,Rahul,76
# S103,Priya,88
# S104,Neha,45
# S105,Amit,58
# S106,Sneha,95
# S107,Karan,81
# S108,Pooja,73
# S109,Rohit,39
# S110,Anjali,90
# Tasks
# 1. Calculate grades for all students.
# 2. Generate a report card file report_card.txt.
# 3. Display topper details.
# 4. Count pass and fail students.
# 5. Display students eligible for merit certificates (marks ≥ 90).


file=open("classwork/python_coding_challenge-1/marks.txt","r")
report=open("classwork/python_coding_challenge-1/report_card.txt","w")

#check if file is opened
if not file:
    exit("file is not opened")

#validation of file either it is empty or not
if not file.read():
    exit("file is empty")

#reset file pointer to beginning after validation
file.seek(0)

#calculate the grade
for line in file:

    #splitting the data
    data=line.strip().split(",")

    marks=int(data[2])
    if marks>=90:
        grade="A"
    elif marks>=80:
        grade="B"
    elif marks>=70:
        grade="C"
    elif marks>=60:
        grade="D"
    else:
        grade="F"
    print(data[0],data[1],grade)

    #writing the data into report card file
    report.write(data[0]+"," + data[1]+"," + data[2]+"," + grade+"\n")


#displaying topper details

#to reset the cursor
file.seek(0)

#initialize variables
topper_id=""
topper_name=""
topper_marks=0

for line in file:

    #splitting the data
    data=line.strip().split(",")
    marks=int(data[2])

    if marks>topper_marks:
        topper_name=data[1]
        topper_id=data[0]
        topper_marks=marks

print("Topper Details :")
print(" ID:",topper_id)
print("Name:",topper_name)
print(" Marks:",topper_marks)


#3.count pass and fail students
file.seek(0)

#initialize variables
pass_count=0
fail_count=0

for line in file:

    #splitting the data
    data=line.strip().split(",")
    marks=int(data[2])

    if marks>=60:
        pass_count+=1
    else:
        fail_count+=1

print("Pass Count:",pass_count)
print("Fail Count:",fail_count)


#5.display students eligible for merit certificates (marks ≥ 90).

#to reset the cursor
file.seek(0)
print("Students eligible for merit certificates :")
for line in file:

    #splitting the data
    data=line.strip().split(",")
    marks=int(data[2])

    if marks>=90:
        print(data[0],data[1],data[2])
