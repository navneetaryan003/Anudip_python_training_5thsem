#program to convert time into corresponding hours , minutes and seconds 

second = int(input("enter the time in sec"))
if(second < 0):
    exit("time cannot be negative ....exited")
#---------------------
hours=0
minutes=0
#convert time to its eqyivalent hour , minute and second
if(second>=3600):
    hours=second//3600
    second=second%3600
if(second>=60):
    minutes=second//60
    second=second%60
#print eqivalent time 
print("equivalent time:",hours,"hours",minutes,"minutes",second,"second")
