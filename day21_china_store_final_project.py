
import torch

product_names = ["A", "B", "C", "D", "E"]

buying_prices = torch.tensor([8, 7, 12, 5, 15])
selling_prices = torch.tensor([15, 12, 20, 8, 25])
quantities_sold = torch.tensor([10, 5, 8, 3, 12])

print("=== China Store Sales Analyzer ===")
print("Products:", product_names)
print("Buying prices:", buying_prices)
print("Selling prices:", selling_prices)
print("Quantities sold:", quantities_sold)




# Task 2: Calculate revenue and profit

revenue = selling_prices * quantities_sold
cost = buying_prices * quantities_sold
profit = revenue - cost

print("\n--- Revenue, Cost, and Profit ---")
print("Revenue:", revenue)
print("Cost:", cost)
print("Profit:", profit)

print("Total revenue:", torch.sum(revenue).item())
print("Total cost:", torch.sum(cost).item())
print("Total profit:", torch.sum(profit).item())



# Task 3: Find the most and least profitable products

best_index = torch.argmax(profit).item()
worst_index = torch.argmin(profit).item()

print("\n--- Profit Analysis ---")
print("Best product:", product_names[best_index])
print("Best profit:", profit[best_index].item())

print("Worst product:", product_names[worst_index])
print("Worst profit:", profit[worst_index].item())




# Task 4: Rank products by profit

sorted_profit, sorted_indices = torch.sort(profit)

print("\n--- Products Ranked by Profit ---")

for i in sorted_indices.tolist():
    print(
        f"Product {product_names[i]}: "
        f"Profit = ${profit[i].item()}"
    )




# Task 5: Calculate profit statistics

average_profit = torch.mean(profit.float())
highest_profit = torch.max(profit)
lowest_profit = torch.min(profit)

above_average = profit > average_profit

print("\n--- Profit Statistics ---")
print("Average profit:", round(average_profit.item(), 2))
print("Highest profit:", highest_profit.item())
print("Lowest profit:", lowest_profit.item())

print("\n--- Above Average Profit ---")
for i, is_above in enumerate(above_average.tolist()):
    if is_above:
        print(f"Product {product_names[i]} is above average")
    else:
        print(f"Product {product_names[i]} is at or below average")





# Task 6: Classify products by profit

profit_status = torch.where(
    profit >= average_profit,
    1,
    0
)

print("\n--- Product Profit Classification ---")

for i, status in enumerate(profit_status.tolist()):
    if status == 1:
        print(f"Product {product_names[i]}: High Profit")
    else:
        print(f"Product {product_names[i]}: Low Profit")

high_profit_count = torch.sum(profit_status).item()
low_profit_count = len(product_names) - high_profit_count

print("\nHigh profit products:", high_profit_count)
print("Low profit products:", low_profit_count)




