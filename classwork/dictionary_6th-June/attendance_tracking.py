# Create Attendance tracker of 30 students. Ask the user to input roll number of student and also
# input whether student is Present or Absent. Store the data in dictionary where roll number will
# be used as a key and Attendance as Value.
# Display the roll number of students who are Present

attendance={}      #taking empty dictionary

for i in range(5):
    roll_number=int(input("enter the roll number :"))
    status=input("enter attendance (Present/Absent) :")

    attendance[roll_number]=status

print("student attendance record :")
print(attendance)

print("Present students :")

for roll_number,status in attendance.items():
    if status.lower()=="present":
        print("present student: ",roll_number)



