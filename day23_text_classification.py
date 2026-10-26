from transformers import pipeline

classifier = pipeline("zero-shot-classification")

customer_message = "The product arrived broken and I want my money back."

labels = [
    "A customer complaint about a product",
    "A customer asking a question",
    "A customer praising a product"
]

result = classifier(
    customer_message,
    candidate_labels=labels
)

print("Message:", customer_message)
print("\nAll categories and scores:")

for label, score in zip(result["labels"], result["scores"]):
    print(label, ":", round(score * 100, 2), "%")