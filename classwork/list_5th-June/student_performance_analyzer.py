#marks of the student
marks=[78,45,92,35,88,40,99,56]

fail_students=0     #failed student conter

highest_marks=marks[0]     #highest marks iniliatisation

lowest_marks=marks[0]      #lowest marks iniliasation

for i in range(0,len(marks)):

    if(marks[i]>=40):           #checking passing marks

        print(marks[i])        #printing passed students

    else:
        fail_students+=1        #counting failed students 

    if(marks[i]>highest_marks):      #finding highest marks 

        highest_marks=marks[i]      #updating highest marks 

    if(marks[i]<lowest_marks):       #finding lowest marks 

        lowest_marks=marks[i]        #updating lowest marks 

print("number of failed students:",fail_students)

print("highest marks",highest_marks)

print("lowest marks",lowest_marks)

new_list=[]     #creating a new list

for i in range(len(marks)):

    if(marks[i]>75):

        new_list.append(marks[i])  #adding the marks in the new list

print(new_list)