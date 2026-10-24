
import torch

product_names = ["A", "B", "C", "D", "E"]

selling_prices = torch.tensor([15, 12, 20, 8, 25])

quantities_sold = torch.tensor([10, 5, 8, 3, 12])

print("Product names:", product_names)
print("Selling prices:", selling_prices)
print("Quantities sold:", quantities_sold)


revenue_per_product = selling_prices * quantities_sold

print("\nRevenue per product:", revenue_per_product)



total_revenue = torch.sum(revenue_per_product)

print("Total business revenue:", total_revenue.item())



best_revenue_index = torch.argmax(revenue_per_product).item()

print("\nBest product by revenue:", product_names[best_revenue_index])
print("Highest revenue:", revenue_per_product[best_revenue_index].item())


sorted_revenue, sorted_indices = torch.sort(revenue_per_product)

print("\n--- Products Ranked by Revenue ---")

for i in sorted_indices.tolist():
    print(f"product {product_names[i]}")
    print(f"revenue = {revenue_per_product[i].item()}")

    
average_revenue = torch.mean(revenue_per_product.float())

print("\nAverage revenue per product:", round(average_revenue.item(), 2))

