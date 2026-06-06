# Write a program to:
# • Display all products costing more than ₹1000.
# • Find the most expensive product.
# • Calculate the total order value.
# • Count products costing below ₹1000.

#details of the order
orders = [
("Laptop", 55000),
("Mouse", 800),
("Keyboard", 1500),
("Monitor", 12000),
("Pen Drive", 600)
]

expensive=orders[0][1]   #counters for holding most expensive product cost

expensive_product=orders[0][0]   #variable that store the expensive product 

sum=0          #for calculating total order value 

count=0         #for counting the products below costing Rs 1000
 

print("Products that costs more than Rs 1000 :")
for record in orders:

    #task1 : Display all products costing more than ₹1000.

    if record[1]>1000:
        print(record[0])
    
    #task4 : Count products costing below ₹1000.
    else:
        count+=1

    #task2 : Find the most expensive product.

    if record[1]>expensive:
        expensive=record[1]
        expensive_product=record[0]

    #task3 : Calculate the total order value.
    sum+=record[1]

print("-----------")
print("Most Expensive Product :",expensive_product)

print("-------------")
print("Total order value : Rs",sum)

print("--------------")
print("number of products costing below 1000 : ",count)