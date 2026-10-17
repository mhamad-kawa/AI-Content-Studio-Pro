import torch

profites = torch.tensor([8.0 , 12.0 , 10.0 , 15.0 , 12.0])

print("profites" , profites)
print("High profit products:" , profites >= 15)
print("Medium profit products:" , (profites >= 10) & (profites < 15))
print("Products needing review:" , profites < 10)

product_names = ["A", "B", "C", "D", "E"]

high_profit_mask = profites >= 15

high_profit_names = [
    product_names[i]
    for i in range(len(product_names))
    if high_profit_mask[i].item()
]

print("High profit product names:", high_profit_names)


medium_profit_mask = (profites >= 10) & (profites < 15)

medium_profit_names = [
    product_names[i]
    for i in range(len(product_names))
    if medium_profit_mask[i].item()
]

print("Medium profit product names:", medium_profit_names)