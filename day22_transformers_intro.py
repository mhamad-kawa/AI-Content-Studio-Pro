
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

reviews = [
    "this product is amazing",
    "I hate this product.",
    "The quality is excellent.",
    "The delivery was terrible."
]

results = sentiment_analyzer(reviews)

print("\n--- Customer Review Analysis ---")


for review, result in zip(reviews, results):
    print("Review:", review)
    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"] * 100, 2), "%")
    print("-" * 40)


positive_count = sum(
    1 for result in results
    if result["label"] == "POSITIVE"
)

negative_count = sum(
    1 for result in results
    if result["label"] == "NEGATIVE"
)


print("Positive reviews:", positive_count)
print("Negative reviews:", negative_count)





total_reviews = len(results)

positive_percentage = (positive_count / total_reviews) * 100

print("Total reviews:", total_reviews)
print("Customer satisfaction:", round(positive_percentage, 2), "%")


if positive_percentage >= 70:
    print("Business recommendation: Keep up the good work!")
elif positive_percentage >= 50:
    print("Business recommendation: Improve your product and service.")
else:
    print("Business recommendation: Urgent improvement needed.")