product = "Wireless Earbuds"
purchase_price = 5
quantity = 100
shipping = 100
selling_price = 10


product = input("enter product name :")

purchase_price = int(input("enter purchase price :"))

quantity = int(input("enter quantity : "))

shipping = int (input("enter shipping cost:"))

selling_price = int(input("enter selling price :"))

product_cost= (purchase_price * quantity)

total_cost= (product_cost + shipping)

total_revenue = (selling_price * quantity)

profit = (total_revenue - total_cost)

profit_margin = (profit/total_revenue*100)


print(product_cost)
print(total_cost)
print(total_revenue)
print(profit)
print(profit_margin)