#write a program to check whether triangle is formed and also identified which type of triangle is formed 

angle1=int(input("enter the first angle"))
if(angle1 <= 0):
    exit("angle1 cannot be negative")
angle2=int(input("enter the second angle"))
if(angle2 <= 0):
    exit("angle2 cannot be negative")
angle3=int(input("enter the third angle"))
if(angle3<=0):
    exit("angle cannot be negative")

#check whether these three angle form a triangle or not
if((angle1 + angle2 + angle3)==180):
  if(angle1<90 and angle2<90 and angle3<90):
      print("above angles formed acute angled triangle")
  elif(angle1 == 90 or angle2 == 90 or angle3 == 90):
      print("above angles form right angled triangle")
  else:
      print("above angles form obtuse angled triangle")
else:
    print("above angles do not form any triangle")