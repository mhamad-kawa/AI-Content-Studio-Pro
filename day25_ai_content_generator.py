from transformers import pipeline

print("Welcome to AI Content Generator!")

generator = pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-135M"
)

print("AI Model is ready!")

topic = input("What topic do you want to write about? ")

if not topic.strip():
    print("Error: Please enter a topic.")
    exit()

print("Your topic:", topic)

prompt = f"""You are an expert business content writer.

Topic: {topic}

Write 3 short and practical tips for beginners.

Rules:
- Every tip must be related to the topic.
- Use simple English.
- Give specific and useful advice.
- Avoid repeating ideas.
- Do not write an introduction or extra steps.

Output requirements:
Write exactly three numbered tips.
Start with Tip 1 and stop after Tip 3.
"""

result = generator(
    prompt,
    max_new_tokens = 70,
    do_sample = True,
    temperature = 0.7,
    return_full_text=False
)

print("\nGenerated Content:")
print(result[0]["generated_text"])