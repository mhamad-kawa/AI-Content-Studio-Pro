
import torch

prices = torch.tensor([5.0, 10.0, 15.0, 20.0, 25.0])
quantities_sold = torch.tensor([20.0, 18.0, 12.0, 8.0, 4.0])

print("Prices:", prices)
print("Quantities sold:", quantities_sold)

price_sales_cor = torch.corrcoef(torch.stack([ prices , quantities_sold]))

print("Price-sales correlation:" , price_sales_cor[0, 1].item())

