import torch

quantities_sold = torch.tensor([10.0, 5.0, 8.0, 3.0, 12.0])

total_sales = torch.sum(quantities_sold)

print("Quantities sold:", quantities_sold)
print("Total units sold:", total_sales.item())

sales_percentage = (quantities_sold/total_sales) * 100

print("Sales percentage per product:" , sales_percentage)

product_names = ["A", "B", "C", "D", "E"]

top_sales_index = torch.argmax(sales_percentage)

print("Top sales product:", product_names[top_sales_index.item()])
print("Sales contribution:", sales_percentage[top_sales_index].item())

sorted_percentages, indices = torch.sort(
    sales_percentage,
    descending=True
)

sorted_names = [
    product_names[i]
    for i in indices.tolist()
]

print("Products ranked by sales percentage:", sorted_names)
print("Sales percentages ranked:", sorted_percentages)