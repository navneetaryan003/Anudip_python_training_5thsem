# Online Shopping Cart Analyzer
# Problem Statement
# The prices of products added to a shopping cart are stored below.
# Sample Data
# cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
# Tasks
# 1. Calculate the total cart value.
# 2. Find the most expensive and cheapest products.
# 3. Count products eligible for premium shipping (price > ₹1000).
# 4. Generate a discount list (products above ₹1500).
# 5. Calculate the average product price.


cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]


#1. Calculate the total cart value.
total_cart_value = sum(cart)
print("Total Cart Value:", total_cart_value)


#2. Find the most expensive and cheapest products.
max_price = max(cart) #max function is used to find the maximum value
min_price = min(cart) #min function is used to find the minimum value
print("Most Expensive Product:", max_price)
print("Cheapest Product:", min_price)


#3. Count products eligible for premium shipping (price > ₹1000).
premium_shipping_count = 0
for price in cart:
    if price > 1000:
        premium_shipping_count += 1
print("Premium Shipping Count:", premium_shipping_count)


#4. Generate a discount list (products above ₹1500).
discount_list = []
for price in cart:
    if price > 1500:
        discount_list.append(price)
print("Discount List:", discount_list)


#5. Calculate the average product price.
average_price = sum(cart) / len(cart)
print("Average Product Price:", average_price)
