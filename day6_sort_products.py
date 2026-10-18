import torch

product_names = ["A" , "B" , "C" , "D" , "E"]

profits = torch.tensor([8.0 , 12.0 , 10.0 , 15.0 , 12.0])

sorted_profits , indices = torch.sort(profits)

sorted_names = [product_names[i] for i in indices.tolist()]



print("Original profits:", profits)
print("Sorted profits:", sorted_profits)
print("Sorted indices:", indices)
print("sorted product names:" , sorted_names)

sorted_profits_desc, indices_desc = torch.sort(
    profits, descending=True
)

sorted_names_desc = [
    product_names[i] for i in indices_desc.tolist()
]

print("Highest to lowest profits:", sorted_profits_desc)
print("Products from highest to lowest:", sorted_names_desc)