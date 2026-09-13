

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
            status = "good"
    
    elif profit_margin >= 15 :
            status = "medium"
    else:
            status= "bad"

    print("status", status) 

    return {
              "name" : product["name"],
              "cost" : product_cost ,
              "revenue" : revenue ,
              "total_cost" : total_cost ,
              "profit" : revenue - total_cost ,
              "profit_margin" : profit / revenue * 100 ,
              "status" : status
              
        }     
     
results = []

for product in products:
    result = analyze_product(product)
    results.append(result)


def calculat_total_profit(results):
     total_profit = 0

     for result in results:
          total_profit = total_profit + result["profit"]
     return total_profit


def calculate_best_profit_and_product(results):
     best_profit = 0
     best_product = ""

     for result in results:
          if result["profit"] > best_profit:
           best_profit = result["profit"]
           best_product = result["name"]
     return best_profit , best_product


def calculate_worst_profit_and_product(results):
     worst_profit = 10000
     worst_product = ""

     for result in results:
          if result["profit"] < worst_profit:
               worst_profit = result["profit"]
               worst_product = result["name"]
     return worst_product , worst_profit

def create_product():
     name = input("product_name:") 
     while True:
      try:
        purchase_price = int(input("purchase price:"))

        if purchase_price <= 0:
            print("Invalid purchase price!")
            continue

        break

      except ValueError:
        print("Please enter a number!")           
     quantity = int (input("quantity:"))
     while quantity <= 0 :
          print("invalid quantity")
          quantity = int(input("quantity:"))
     shipping = int(input("shipping:"))
     while shipping < 0 :
          print("invalid shipping")
          shipping = int(input("shipping: "))
     selling_price = int(input("selling price:"))
     while selling_price <= 0 :
          print("invalid selling price")
          selling_price = int (input("selling price:"))


     product = {
     "name" : name,
     "purchase_price" : purchase_price,
     "quantity" : quantity ,
     "shipping" : shipping ,
     "selling_price" : selling_price     
}
     return product
new_product = create_product()
products.append(new_product)


new_result = analyze_product(new_product)
results.append(new_result)

def final_report(results):
    total_profit = calculat_total_profit(results)
    print("Total Profit:", total_profit)
    best_profit, best_product = calculate_best_profit_and_product(results)
    print("Best Product:", best_product)
    print("Best Profit:", best_profit)
    worst_product, worst_profit = calculate_worst_profit_and_product(results)

    print("Worst Product:", worst_product)
    print("Worst Profit:", worst_profit)

    print("\nProduct Decisions:")

    for result in results:
        if result["profit_margin"] >= 40:
            decision = "Scale"
        elif result["profit_margin"] >= 30:
            decision = "Keep"
        else:
            decision = "Review"

        print(result["name"], "→", decision)


final_report(results) 