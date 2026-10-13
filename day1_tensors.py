import torch

import torch

numbers = torch.tensor([10, 20, 30, 40, 50])

print("Numbers:", numbers)
print("First number:", numbers[0])
print("Total:", numbers.sum())
print("Average:", numbers.float().mean())
print("Shape:", numbers.shape)