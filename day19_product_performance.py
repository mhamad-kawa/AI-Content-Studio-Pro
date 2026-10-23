
import torch

product_names = ["A", "B", "C", "D", "E"]

quantities_sold = torch.tensor([10, 5, 8, 3, 12])

sales_target = 7

print("Product names:", product_names)
print("Quantities sold:", quantities_sold)
print("Sales target:", sales_target)



sales_status = quantities_sold >= sales_target

print("\nSales status:", sales_status)


successful_indices = torch.where(sales_status)[0]

print("\nProducts that achieved the sales target:")

for i in successful_indices.tolist():
    print (f"product {product_names[i]}: {quantities_sold[i].item()} units")




failed_indices = torch.where(~sales_status)[0]

print("\nProducts below the sales target:")

for i in failed_indices.tolist():
    print(f"Product {product_names[i]}: {quantities_sold[i].item()} units")





successful_count = torch.sum(sales_status).item()
failed_count = torch.sum(~sales_status).item()

print("\n--- Sales Performance Summary ---")
print("Successful products:", successful_count)
print("Products below target:", failed_count)




total_products = len(product_names)

success_rate = (successful_count / total_products) * 100

print("Total products:", total_products)
print(f"Sales target success rate: {success_rate:.1f}%")
