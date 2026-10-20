
import torch

quantities_sold = torch.tensor([10.0, 5.0, 8.0, 3.0, 12.0])

average_sales = torch.mean(quantities_sold)

print("Quantities sold:", quantities_sold)
print("Average sales:", average_sales.item())


sales_std = torch.std(quantities_sold)
print(f"Average sales rounded: {average_sales.item(): .2f}")

sales_range = torch.max(quantities_sold) - torch.min(quantities_sold)
print("sales range :" , sales_range.item())


