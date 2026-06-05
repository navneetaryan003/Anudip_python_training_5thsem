#write a program to execute the inventory stock alert

stock=[25,5,0,12,3,18,0,30]

out_of_stock=0     #for tracking the products out of stock

restock_req=[]   #creating a list of product that is required to restock

available=0  #for tracking available products 

healthy_stock=[]   #creating a list to store healthy products 

for i in range(len(stock)):

    if(stock[i]==0):
        out_of_stock+=1     #counting the product that are out of stock

    if(stock[i]<10):
        restock_req.append(stock[i])    #adding items that need to restock

    if(stock[i]>0):
        available+=1   #counting the available products

    if(stock[i]>=15):
        healthy_stock.append(stock[i])    #adding items that are enough in inventory

print("out of stock products:",out_of_stock)

print("restock required:",restock_req)

print("Available Products:",available)

print("Healthy Stock:",healthy_stock)