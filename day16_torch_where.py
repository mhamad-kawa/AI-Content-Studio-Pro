import torch

product_names = ["A", "B", "C", "D", "E"]

quantities_sold = torch.tensor([10, 5, 8, 3, 12])

sales_target = 7

status = torch.where(
    quantities_sold > sales_target ,
    1 ,
    0
)

print("quantities sold" , quantities_sold)
print("status" , status)


status = torch.where(
    quantities_sold > sales_target,
    1,
    0
)

status_names = {
    1 : "Target achieved",
    0 : "Needs improvement" 
}

for i in range(len(product_names)):
    print(f"product {product_names[i]}:  {status_names [status[i].item()]}")

successful_indices = torch.where(quantities_sold > sales_target)[0]

successful_products = [
    product_names[i]
    for i in successful_indices.tolist()
]

print("Successful products:", successful_products)

successful_count = successful_indices.numel()

print("Number of successful products:", successful_count)

success_percentage = (successful_count / len(product_names)) * 100

print(f"Success rate: {success_percentage:.1f}%")



below_target_count = (quantities_sold <= sales_target).sum().item()

print("\n--- Sales Summary ---")
print(f"Total products: {len(product_names)}")
print(f"Successful products: {successful_count}")
print(f"Products at/below target: {below_target_count}")
print(f"Success rate: {success_percentage:.1f}%")