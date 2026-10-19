import torch

quantities_sold = torch.tensor([10.0, 5.0, 8.0, 3.0, 12.0])

average_sales = torch.mean(quantities_sold)

print("quantities sold:" , quantities_sold)
print("average sales per product:" , average_sales)

product_names = ["A", "B", "C", "D", "E"]

above_average = quantities_sold > average_sales

print("Above average mask:", above_average)


above_average_names = [
    product_names [i]
    for i in range(len(product_names))
    if above_average[i].item()
]

print("Products above average:", above_average_names)

lowest_sales_index = torch.argmin(quantities_sold)

print("Lowest sales product:", product_names[lowest_sales_index.item()])
print("Lowest quantity sold:", quantities_sold[lowest_sales_index].item())


highest_sales = torch.max(quantities_sold)
lowest_sales = torch.min(quantities_sold)

sales_difference = highest_sales - lowest_sales

print("Highest sales:", highest_sales.item())
print("Lowest sales:", lowest_sales.item())
print("Sales difference:", sales_difference.item())