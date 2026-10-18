import torch

purchase_prices = torch.tensor([10.0, 20.0, 15.0, 30.0, 8.0])
selling_prices = torch.tensor([18.0, 32.0, 25.0, 45.0, 20.0])

quantities_sold = torch.tensor([10.0, 5.0, 8.0, 3.0, 12.0])


profit_per_product = selling_prices - purchase_prices

total_profits = profit_per_product * quantities_sold

print("profit per product : " , profit_per_product)
print("quantities sold : " , quantities_sold)
print("total profits per product :" , total_profits)
print("total busnes product :" , total_profits.sum())


product_names = ["A", "B", "C", "D", "E"]

best_index = torch.argmax(total_profits)
print("Most profitable product:", product_names[best_index.item()])
print("Its total profit:", total_profits[best_index])




sorted_total_profits , indices = torch.sort(total_profits , descending=True)

sorted_names = [product_names[i] for i in indices.tolist()]

print("Products ranked by total profit:" , sorted_names)
print("Total profits ranked:" , sorted_total_profits)

total_quantity_sold = quantities_sold.sum()

print("Total quantity sold:", total_quantity_sold.item())