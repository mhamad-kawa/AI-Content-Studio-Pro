
products = ["Wireless Earbuds", "Smart Watch", "Bluetooth Speaker"]
print(products[0])
print(products[2])

products.append("USB-C Cable")
print(products)

for product in products:
    print(product)



product = {
        "name": "Wireless Earbuds",
        "purchase_price": 5,
        "quantity": 100,
        "shipping": 100,
        "selling_price": 10

    }
print(product["quantity"])
print(product["selling_price"])


product_cost = product["purchase_price"]*product["quantity"]
print(product_cost)

total_cost = product["shipping"] + product_cost
print(total_cost)

revenue = product["quantity"] * product["selling_price"]
print(revenue)

profit = revenue - total_cost
print(profit)




for product in products:

    product_cost = product["purchase_price"] * product ["quantity"]
    revenue = product ["selling_price"] * product ["quantity"]
    total_cost = product_cost + product["shipping"]
    profit =  revenue - total_cost
    profit_margin = profit /  revenue * 100

    if profit_margin>= 30 :
        print("Status:" ,"good")

    elif profit_margin >= 15 :
        print("Status:" ,"mediam")
    else:
        print("Status:" ,"bad")
    
    print(product["name"])
    print("Cost:" , product_cost)
    print("Revenue:", revenue)
    print("Total Cost:" , total_cost)
    print("Profit:" ,profit)
    print("Profit Margin:",profit_margin)
