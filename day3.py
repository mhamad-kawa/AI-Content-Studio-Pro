

def calculate_product_cost(purchase_price,quantity):
    return quantity*purchase_price
purchase_price = int(input("enter to purchase_price:"))
quantity = int (input("enter to quantity:"))
product_cost = calculate_product_cost(purchase_price,quantity)
print(product_cost)



def calculate_total_cost(product_cost,shipping):
    return product_cost+shipping
shipping = int(input("enter to shipping : "))
total_cost = calculate_total_cost(product_cost,shipping)
print(total_cost)

def calculate_revenue(selling_price,quantity):
    return selling_price*quantity
selling_price = int(input("enter to selling_price : "))
total_revenue = calculate_revenue(selling_price,quantity)
print(total_revenue)

def calclate_profit(total_revenue,total_cost):
    return total_revenue-total_cost
profit = calclate_profit(total_revenue,total_cost)
print(profit)

def calculate_profit_margin(profit,total_revenue):
    return profit/total_revenue*100
calculate_margin = calculate_profit_margin(profit,total_revenue)
print(calculate_margin)

if calculate_margin >= 30 :
    print("good")
elif calculate_margin >=15:
    print ("mediam")
else:
    print("nogood")


def analyze_product():
   
    print("Analyze_product")
analyze_product()

