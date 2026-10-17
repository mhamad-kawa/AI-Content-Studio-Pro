import torch

purchase_price = torch.tensor([10.0, 20.0, 15.0, 30.0, 8.0])
selling_price = torch.tensor([18.0, 32.0, 25.0, 45.0, 20.0])

profits = selling_price - purchase_price

print("Product profits:", profits)
print("Highest profit:", torch.max(profits))
print("Lowest profit:", torch.min(profits))
print("Best product index:", torch.argmax(profits))
print("Best product:" , ["A","B","C","D","E"][torch.argmax(profits).item()])
print("Worst product index:", torch.argmin(profits))
print("Worst product:", ["A", "B", "C", "D", "E"][torch.argmin(profits).item()])