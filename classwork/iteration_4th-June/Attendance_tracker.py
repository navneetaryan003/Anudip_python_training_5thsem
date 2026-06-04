#write a program to count the no of student present or absent

total_students=30
attendance_count=1
present_count=0

while(attendance_count<=30):
    
    print("student",attendance_count)
    
    #input for student present or not 
    student_present=input("Attendance:")

    #count the present student

    if(student_present.lower()=="present"):
          present_count+=1
    
         
          
    attendance_count+=1   


print("No of present student:",present_count) 
print("no of absent student:",total_students-present_count)