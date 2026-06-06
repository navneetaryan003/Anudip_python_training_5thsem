# Write a program to:
# • Count present and absent days.
# • Calculate attendance percentage.
# • Determine eligibility (minimum 75% attendance).
# • Display positions where the student was absent.

#list of present and absent 
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

count_present=0     #counter for counting present student
count_absent=0      #counter for counting absent student

for i in range(len(attendance)):

    #task 1:Count present and absent days.
    if attendance[i].upper()=="P":
        count_present+=1
    
    else:
        count_absent+=1

print("Present Student : ",count_present)

print("Absent Student :",count_absent)

#task 2:Calculate attendance percentage.
attendance_percentage=(count_present/len(attendance))*100

print(f"Attendance Percantage : {attendance_percentage:.2f}")

#task 3:Determine eligibility (minimum 75% attendance).
if attendance_percentage>=75:
    print("student is eligible")
else:
    print("student is not eligible")

#task4:Display positions where the student was absent.
absent_pos=[]
for i in range(len(attendance)):
     if attendance[i].upper()=="A":
         absent_pos.append(i+1)

print("position of student where the student was absent :",absent_pos)
