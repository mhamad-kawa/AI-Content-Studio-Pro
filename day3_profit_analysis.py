import torch

purchase_price = torch.tensor([10.0,20.0,15.0,30.0,8.0])
selling_price = torch.tensor([18.0,32.0,25.0,45.0,20.0])

profits = selling_price - purchase_price


print("profites :", profits)
print("Total profit:", profits.sum())
print("Average profit:", profits.mean())