

product = {
    "name": "smart_watch",
    "purchase_price" : 20 ,
    "quantity" : 50 ,
    "shipping" : 100 ,
    "selling_price" : 40
}

product2 = {
    "name":"Bluetooth Speaker",
    "purchase_price":15 ,
    "quantity": 30 ,
    "shipping": 80 ,
    "selling_price": 30 ,
    
}


product3 = {
    "name": "USB-C Cable",
    "purchase_price": 3,
    "quantity": 100,
    "shipping": 50,
    "selling_price": 7
}

products = [product ,product2 , product3]


def analyze_product(product):

    print("Product:", product["name"])
    
    product_cost = product["purchase_price"] * product ["quantity"]
    print("Cost:", product_cost)

    revenue = product ["selling_price"] * product ["quantity"]
    print("Revenue:", revenue)

    total_cost = product_cost + product["shipping"]
    print("Total Cost:", total_cost)

    profit =  revenue - total_cost
    

    profit_margin = profit /  revenue * 100
   

    if profit_margin>= 30 :
            Status= "good"
    
    elif profit_margin >= 15 :
            Status= "mediam"
    else:
            Status= "bad"

    print("Status:", Status) 

    return {
              "name" : product["name"],
              "cost" : product_cost ,
              "revenue" : revenue ,
              "total_cost" : total_cost ,
              "profit" : revenue - total_cost ,
              "profit_margin" : profit / revenue * 100 ,
              "status" : Status
              
        }     
     
results = []

for product in products:
    result = analyze_product(product)
    results.append(result)

for result in results:
    print("Product:", result["name"])
    print("Profit:", result["profit"])
    print("Margin:", result["profit_margin"], "%")
    print("Status:", result["status"])
    print()



total_profit = 0

for result in results:
    total_profit = total_profit + result["profit"]

print("total_profit" , total_profit)      


best_profit = 0
best_product = ""

for result in results:
    if result["profit"] > best_profit:
          best_profit = result["profit"]
          best_product = result["name"]
print("Best Product:", best_product)
print("Best profit" , best_profit)          

    
worst_profit = 100000
worst_product = ""

for result in results:
      if result["profit"] < worst_profit:
            worst_profit = result["profit"]
            worst_product= result["name"]

print("worst profit" , worst_profit)
print("worst product" , worst_product)  

for result in results:
      
      
      
      if result["profit_margin"] >= 40 :
            decision = "scale"
      elif result["profit_margin"] >= 30 :
            decision = "keep"       
      else:
             decision = "review"
      result["decision"] = decision  
      print(result)


for result in results:
      print("=======================")
      print("proudect" , result["name"])
      print("profit" , result["profit"])
      print("margin" , result["profit_margin" ], "%")
      print("status" , result["status"])
      print("decision" , result["decision"])


name = input("product name : ")
purchase_price = int(input("purchase price : "))
while purchase_price <= 0:
    print("Invalid purchase price. Try again.")
    purchase_price = int(input("purchase price : "))
quantity = int(input("quantity : "))
while quantity <= 0:
     print("Invalid quality. Try again.")
     quantity = int(input("quality :"))
shipping = int(input("shipping : "))
while shipping < 0 :
     print("invalid shipping. try again.")
     shipping = int(input("shipping :"))
selling_price = int(input("selling price : "))
while selling_price <= 0 :
     print("invalid selling price. try again.")
     selling_price = int(input("selling price :"))

product = {
      "name" : name,
      "purchase_price" : purchase_price,
      "quantity" : quantity,
      "shipping" : shipping , 
      "selling_price" : selling_price 
}
result = analyze_product(product)
results.append(result)
total_profit = 0

for result in results:
    total_profit = total_profit + result["profit"]

print("total_profit", total_profit)


best_profit = 0
best_product = ""

for result in results:
    if result["profit"] > best_profit:
        best_profit = result["profit"]
        best_product = result["name"]

print("Best Product:", best_product)
print("Best profit", best_profit)

for result in results:
    if result["profit_margin"] >= 40:
        decision = "scale"
    elif result["profit_margin"] >= 30:
        decision = "keep"
    else:
        decision = "review"

    result["decision"] = decision


for result in results:
    print("=======================")
    print("Product:", result["name"])
    print("Profit:", result["profit"])
    print("Margin:", result["profit_margin"], "%")
    print("Status:", result["status"])
    print("Decision:", result["decision"])

profits = [result["profit"] for result in results]
for result in results:
     if result["profit"] == best_profit:
      best_product = result["name"]
    
print("Max Profit:", max(profits))
print("Min Profit:", min(profits))
print("best profit" , best_profit)
print("Best Product:", best_product)