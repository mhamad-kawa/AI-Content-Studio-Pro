
import torch

product_names = ["A", "B", "C", "D", "E"]

selling_prices = torch.tensor([15, 12, 20, 8, 25])
cost_prices = torch.tensor([10, 7, 12, 5, 15])
quantities_sold = torch.tensor([10, 5, 8, 3, 12])

profit_per_unit = selling_prices - cost_prices

total_profit = profit_per_unit * quantities_sold

print("Profit per unit:", profit_per_unit)
print("Total profit per product:", total_profit)


total_business_profit = torch.sum(total_profit)
print("total_business_profit " , total_business_profit.item())


best_profit_index = torch.argmax(total_profit).item()

print("Most profitable product:" , product_names[best_profit_index])
print("Highest total profit:" , total_profit[best_profit_index].item())


sorted_profit, sorted_indices = torch.sort(total_profit)

print("\n--- Products Ranked by Total Profit ---")

for i in sorted_indices.tolist():
    print(
        f"product {product_names[i]}:"
        f"profit = {total_profit[i].item()}"
    )


    profit_margin = (
    profit_per_unit.float() / selling_prices.float()
) * 100

print("\n--- Profit Margin per Product ---")

for i in range(len(product_names)):
    print(
        f"Product {product_names[i]}: "
        f"{profit_margin[i].item():.1f}%"
    )



    average_profit = torch.mean(total_profit.float())

print("\n--- Business Summary ---")
print("Number of products:", len(product_names))
print("Total business profit:", total_business_profit.item())
print("Average profit per product:", round(average_profit.item(), 2))
print("Best product:", product_names[best_profit_index])
print("Best product profit:", total_profit[best_profit_index].item())