
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-135M"
)

prompt = "Three practical tips for young people starting an online business:"

result = generator(
    prompt,
    max_new_tokens=100,
    do_sample=True,
    temperature=1.2

)

print("\nGenerated Text:")
print(result[0]["generated_text"])

