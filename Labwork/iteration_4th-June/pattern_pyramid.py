#write a program to print the pattern
#input the number of rows from user 
rows=int(input("enter the number of rows:"))

for i in range(1,6):  #controls the number of row
    for j in range(1,i+1):  #controls the number of column 
        print(j,end="")
    print()


for i in range(rows,0,-1):    #controls the number of row
    for k in range(1,i+1):      #controls the number of column
        print(k,end="")
    print()        

    