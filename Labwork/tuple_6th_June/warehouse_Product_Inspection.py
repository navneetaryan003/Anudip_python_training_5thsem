# Write a program to:
# • Display failed product IDs.
# • Count passed and failed products.
# • Calculate pass percentage.
# • Stop checking if 3 failures are found.

#details of the product
products = [
(101, "Pass"),
(102, "Fail"),
(103, "Pass"),
(104, "Fail"),
(105, "Pass")
]


count_fail=0     #counter for counting fail student 
count_pass=0      #counter for counting pass student

for product in products:

    #task 1:Display failed product IDs.
    if product[1].capitalize()=="Fail":
        print(product[0])

        #task 2 : Count passed and failed products.
        count_fail+=1
    
    else:
        count_pass+=1

# task 3 :Calculate pass percentage.
percentage=(count_pass/len(products))*100
print("Pass percentage :",percentage)


#task 4 : Stop checking if 3 failures are found.
for product in products:
    if count_fail==3:
        print("3 failures found")
        break
else:
    print("there is no failures equal to 3")
    