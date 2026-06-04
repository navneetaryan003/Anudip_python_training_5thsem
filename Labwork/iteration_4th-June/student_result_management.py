#write a program to display the grade of the student according to the marks  

total_full_marks=0      #initailisation of total marks to calculate 
total_obtained_marks=0    #initailisation of obtained marks to calculate
fail_subject=0           #initialisation of number of failed subject

for i in range(1,3):

    # enter the subject full marks 

    print("enter the full marks in subject",i,":")
    full_marks=int(input())

    #enetr the subject obtained marks 

    print("enter the obtained marks in subject",i,":")
    obtained_marks=int(input())

    #enter the subject passing marks 

    print("enter the passing marks in subject",i,":")
    passing_marks=int(input())

    total_full_marks += full_marks #calculating total full marks in subjects 

    if(obtained_marks<0):  #validation of obtained marks
        continue
    elif(obtained_marks<full_marks):
        total_obtained_marks+=obtained_marks    #calculating obtained marks in subjects  
    else:
        print("obtained marks is not valid")
    
    #validation either student will failed in subject or not

    if(obtained_marks==0 or obtained_marks<passing_marks):
        print("student will failed in subject",i)
        fail_subject+=1      #count the failed subject

percentage=(obtained_marks/full_marks)*100    #calculating percentage 

#distributed grade on the basis of percentage 

if(percentage>=90):
    print("Grade:A+")
elif(percentage>=75):
    print("Grade:A")
elif(percentage>=60):
    print("Grade:B")    
elif(percentage>=40):
    print("Grade:C")
else:
    print("Grade:fail")    

#displaying total number of failed subjects 

print("total number of failed subject:",fail_subject)