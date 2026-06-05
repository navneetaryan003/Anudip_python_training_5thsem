#write a program to calculate transaction history 

transactions=[5000,-2000,3000,-1000,-500,7000]

balance=0    #initialisation of balance 

deposits=[]     #creating a list for deposits transaction
withdrawals=[]    #creating a list for withdrawals transaction

largest_deposits=transactions[0]    #assuming largestest deposits 

largest_withdrawals=transactions[0]   #assuming largest withdrawals 

for i in range(len(transactions)):
    balance+=transactions[i]         #calculating total balance 
    
    if(transactions[i]==0):           #validating transaction is happened or not 
        print("no deposits and withdrawals")

    elif(transactions[i]>0):         

        deposits.append(transactions[i])    #adding deposits to deposits list
    
    else: 
         
        withdrawals.append(transactions[i])     #adding withdrawals in withdrawals list

    if(transactions[i]>largest_deposits):
        largest_deposits=transactions[i]     #calculating the largest deposits 
    
    if(transactions[i]<largest_withdrawals):
        largest_withdrawals=transactions[i]     #calculating the largest withdrawals 

print("Current Balance:",balance)

print("Deposits",deposits)

print("Withdrawals",withdrawals)

print("Largest Deposits",largest_deposits)

print("Largest Withdrawals",largest_withdrawals)



    