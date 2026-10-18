import torch

purchase_prices = torch.tensor([10.0, 20.0, 15.0, 30.0, 8.0])
selling_prices = torch.tensor([18.0, 32.0, 25.0, 45.0, 20.0])

profits = selling_prices - purchase_prices

profit_margin = (profits / selling_prices) * 100

print("Profits:", profits)
print("Profit margins:", profit_margin)

best_margin_index = torch.argmax(profit_margin)

product_names = ["A", "B", "C", "D", "E"]

print("Best profit margin:", profit_margin[best_margin_index])
print("Best product:", product_names[best_margin_index.item()])

sorted_margins, margin_indices = torch.sort(
    profit_margin, descending=True
)

sorted_names = [
    product_names[i] for i in margin_indices.tolist()
]

print("Margins from highest to lowest:", sorted_margins)
print("Products by profit margin:", sorted_names)