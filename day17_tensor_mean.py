import torch

product_names = ["A", "B", "C", "D", "E"]

quantities_sold = torch.tensor([10 , 5 , 8 , 3 , 12])

average_sales = torch.mean(quantities_sold.float())

print("Quantities sold:", quantities_sold)
print("Average sales:", round(average_sales.item(), 2))


max_sales = torch.max(quantities_sold)
min_sales = torch.min(quantities_sold)

max_index = torch.argmax(quantities_sold).item()
min_index = torch.argmin(quantities_sold).item()


print("Highest sales:", max_sales.item())
print("Best-selling product:", product_names[max_index])

print("Lowest sales:", min_sales.item())
print("Lowest-selling product:", product_names[min_index])

sorted_sales, sorted_indices = torch.sort(quantities_sold)

print("Sorted sales:", sorted_sales)
print("Products from lowest to highest:")

for i in sorted_indices.tolist():
    print(f"Product {product_names[i]}: {quantities_sold[i].item()}")


total_sales = torch.sum(quantities_sold)

print("Total units sold:", total_sales.item())   


sales_difference = quantities_sold.float() - average_sales

print("\n--- Sales Difference from Average ---")

for i in range(len(product_names)):
    print(
        f"product {product_names[i]}:"
        f"{sales_difference[i].item():+.1f}"
    )


sales_status = torch.where(
    quantities_sold.float() > average_sales,
    1,
    torch.where(
        quantities_sold.float() < average_sales ,
        -1,
        0
    )
)

print("\n--- Product Performance ---")

for i in range(len(product_names)):
    if sales_status[i].item() == 1 :
        label = "Above average"
    elif sales_status[i].item() == -1:
        label = "Below average"
    else:
        label = "Equal to average"


    print(f"product {product_names[i]} : {label}")            
