# An e-commerce company stores product sales data as:
# sales = {
# "Laptop": 15,
# "Mouse": 45,
# "Keyboard": 32,
# "Monitor": 12,
# "Headphones": 28,
# "Printer": 8,
# "Webcam": 20,
# "Speaker": 18,
# "Tablet": 10,
# "Router": 25
# }
# Tasks
# 1. Display products sold more than 20 times.
# 2. Find the best-selling product.
# 3. Find the least-selling product.
# 4. Calculate total products sold.
# 5. Create a list of products requiring promotion (sales < 15).
# 6. Count products having sales between 10 and 30.

#--------------------------------------------------------
sales = {
"Laptop": 15,
"Mouse": 45,
"Keyboard": 32,
"Monitor": 12,
"Headphones": 28,
"Printer": 8,
"Webcam": 20,
"Speaker": 18,
"Tablet": 10,
"Router": 25
}

#------------------------------------------------------
#task 1: display products sold more than 20 times

print("Products sold more than 20 times:")
for product, quantity in sales.items():
    if quantity > 20:
        print(f"{product}: {quantity}")

#------------------------------------------------------
#task 2: find the best-selling product
sales_items = list(sales.items())

best_selling_product = sales_items[0]

for product, quantity in sales_items:
    if quantity > best_selling_product[1]:
        best_selling_product = (product, quantity)

print(f"\nBest-selling product: {best_selling_product[0]} with {best_selling_product[1]} sales")

#------------------------------------------------------
#task 3: find the least-selling product
least_selling_product = sales_items[0]
for product, quantity in sales_items:
    if quantity < least_selling_product[1]:
        least_selling_product = (product, quantity)

print(f"\nLeast-selling product: {least_selling_product[0]} with {least_selling_product[1]} sales")

#------------------------------------------------------
#task 4: calculate total products sold
total_products_sold = 0
for quantity in sales.values():
    total_products_sold += quantity

print(f"\nTotal products sold: {total_products_sold}")

#------------------------------------------------------
#task 5: create a list of products requiring promotion (sales < 15)
products_requiring_promotion = []
for product, quantity in sales.items():
    if quantity < 15:
        products_requiring_promotion.append(product)

print(f"\nProducts requiring promotion: {products_requiring_promotion}")

#------------------------------------------------------
#task 6: count products having sales between 10 and 30
count_products_between_10_and_30 = 0
for quantity in sales.values():
    if 10 <= quantity <= 30:
        count_products_between_10_and_30 += 1

print(f"\nNumber of products with sales between 10 and 30: {count_products_between_10_and_30}")

#------------------------------------------------------




'''Output:
Products sold more than 20 times:
Mouse: 45
Keyboard: 32
Headphones: 28
Router: 25          
Best-selling product: Mouse with 45 sales       
Least-selling product: Printer with 8 sales
Total products sold: 213
\nProducts requiring promotion: ['Monitor', 'Printer', 'Tablet']
Number of products with sales between 10 and 30: 6
'''