#write a program to count the no of student present or absent


total_students=30      #initialisation of number of student
attendance_count=1     #attendance counter
present_count=0        #present student record counter

while(attendance_count<=30):
    
    print("student",attendance_count)
    
    #input for student present or not 
    student_present=input("Attendance:")

    #count the present student

    if(student_present.lower()=="present"):  #lower function is to convert input into lowercase 
          present_count+=1
    
         
          
    attendance_count+=1   

#displaying the number of present student and absent student in the class 

print("No of present student:",present_count) 
print("no of absent student:",total_students-present_count)