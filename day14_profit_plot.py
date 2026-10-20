
import torch
import matplotlib.pyplot as plt

product_names = ["A", "B", "C", "D", "E"]

purchase_prices = torch.tensor([10.0, 20.0, 15.0, 30.0, 8.0])
selling_prices = torch.tensor([18.0, 32.0, 25.0, 45.0, 20.0])

profits = selling_prices - purchase_prices

print("Product profits:", profits)
print("Total profit:", profits.sum().item())

best_index = torch.argmax(profits)

print("Best product:", product_names[best_index.item()])
print("Highest profit:", profits[best_index].item())




sorted_profits, indices = torch.sort(profits, descending=True)

sorted_names = [
    product_names[i]
    for i in indices.tolist()
]

print("Products ranked by profit:", sorted_names)
print("Profits ranked:", sorted_profits.tolist())


bars = plt.bar(product_names, profits.tolist())

plt.bar_label(bars, fmt="$%.0f")
plt.title("Profit per Product")
plt.xlabel("Product")
plt.ylabel("Profit ($)")

plt.tight_layout()
plt.savefig("day14_profit_plot.png")
plt.show()

