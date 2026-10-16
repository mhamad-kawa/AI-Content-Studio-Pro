import torch

products = torch.tensor([
    [10 , 15],
    [20 , 30],
    [5 , 12]
])

print("product data:")
print(products)

print("Shape:", products.shape)
print("Dimensions:", products.ndim)
print("Total values:", products.numel())
print("First product purchase price:", products[1, 0])