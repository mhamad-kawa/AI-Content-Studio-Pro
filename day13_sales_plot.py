import torch
import matplotlib.pyplot as plt

prices = torch.tensor([5.0, 10.0, 15.0, 20.0, 25.0])
quantities_sold = torch.tensor([20.0, 18.0, 12.0, 8.0, 4.0])
product_names = ["A", "B", "C", "D", "E"]

plt.plot(
    prices.tolist(),
    quantities_sold.tolist(),
    marker="o",
    color="green",
    linestyle="--"
)

for i in range(len(product_names)):
    plt.annotate(
        product_names[i],
        (prices[i].item(), quantities_sold[i].item())
    )


plt.title("Product Price vs. Quantity Sold")
plt.xlabel("price $")
plt.ylabel("quantity sold")

plt.grid(True)
plt.tight_layout()


plt.savefig("day13_sales_plot.png")
plt.show()