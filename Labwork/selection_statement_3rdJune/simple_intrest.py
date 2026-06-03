principal= int(input("enter the principal ammount(in Rs):"))
if(principal < 0):
    exit("pricipal cannot be negative")
rate = int(input("enter the rate (in percentage): "))
if(rate < 0):
    exit("rate cannot be negative")
time = int(input("enter the time (in years):"))
if(time < 0):
    exit("time cannot be negative")

si = (principal*rate*time)/100
print("simple intrest",si,"Rs") 