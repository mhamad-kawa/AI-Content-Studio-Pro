import torch

purchase_prices = torch.tensor([12.0, 25.0, 40.0])
selling_prices = torch.tensor([20.0, 35.0, 55.0])

profits = selling_prices - purchase_prices

print("purchase price:" , purchase_prices)
print("selling price:" , selling_prices)
print("profits:" , profits)
print("total profits:" , profits.sum())
print("avrege profits:" , profits.mean())