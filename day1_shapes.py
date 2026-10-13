import torch

number = torch.tensor(7)

vector = torch.tensor([10,20,30])

matrix = torch.tensor([
    [1,2,3],
    [4,5,6]
])

print("number:", number.shape , number.ndim)
print("vector:", vector.shape , vector.ndim)
print("matrix:", matrix.shape , matrix.ndim)