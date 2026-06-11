# Employee Attendance Monitoring System
# Problem Statement
# Employee attendance records are stored in attendance.txt.
# Sample Input/Data (attendance.txt)
# EMP101,P
# EMP102,A
# EMP103,P
# EMP104,P
# EMP105,A
# EMP106,P
# EMP107,P
# EMP108,A
# EMP109,P
# EMP110,P
# Tasks
# 1. Count present and absent employees.
# 2. Display absent employee IDs.
# 3. Calculate attendance percentage.
# 4. Generate an absentee report in absent_report.txt.
# 5. Display employees eligible for attendance awards (100% attendance).


file=open("classwork/python_coding_challenge-1/attendance.txt","r")
report=open("classwork/python_coding_challenge-1/absent_report.txt","w")

#check if file is opened
if not file:
    exit("file is not opened")

#validation of file either it is empty or not
if not file.read():
    exit("file is empty")

#count of present employees
count_present=0  #count of present employees
count_absent=0   #count of absent employees

file.seek(0)  #set the file cursor to the beginning

for line in file:

    #splitting the data
    line=line.strip().split(",")        

    if line[1]=="P":
        count_present+=1
    else:
        count_absent+=1


print("Present : ",count_present)
print("Absent : ",count_absent)


#2.display absent employee ID
file.seek(0)

print("Absent Employee IDs : ")
for line in file:

    #splitting the data
    line=line.strip().split(",")        

    if line[1]=="A":
        print(line[0])


#3.calculate attendance percentage
attendance_percentage=(count_present/(count_present+count_absent))*100

print("Attendance Percentage : ",attendance_percentage)


#4.generate absentee report
file.seek(0)

for line in file:

    #splitting the data
    line=line.strip().split(",")        

    if line[1]=="A":
        report.write(line[0]+"\n")


#5.display employees eligible for attendance awards (100% attendance)
file.seek(0)

print("Employees eligible for attendance awards : ")
for line in file:

    #splitting the data
    line=line.strip().split(",")        

    if line[1]=="P":
        print(line[0])



