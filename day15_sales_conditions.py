import torch

product_name = ["A" , "B" , "C" , "D" , "E"]

quantities_sold = torch.tensor([10 ,5 , 8, 3, 12])

sales_target = 7

above_target = quantities_sold > sales_target

print("Quantities sold:", quantities_sold)
print("Sales target:", sales_target)
print("Above target:", above_target)

successful_products = [
    product_name [i]
    for i in range(len(product_name))
    if above_target[i].item()
]

print("Products above target:" , successful_products)

successful_count = above_target.sum().item()

print("Number of products above target:", successful_count)

total_product = len(product_name)

success_percentage = (successful_count/total_product)*100

print(f"Success percentage: {success_percentage:.1f}%")


below_target = quantities_sold < sales_target

low_sales_products = [
    product_name[i]
    for i in range(len(product_name))
    if below_target[i].item()
]

print("Products below target:", low_sales_products)


for i in range(len(product_name)):
    if above_target[i].item():
        status = "Target achieved"
    else:
        status = "Needs improvement"
    print(f"product{product_name[i]:} , {status}")  



    below_count = below_target.sum().item()

print("\n--- Sales Summary ---")
print(f"Products meeting target: {successful_count}")
print(f"Products needing improvement: {below_count}")
print(f"Overall success rate: {success_percentage:.1f}%")  

