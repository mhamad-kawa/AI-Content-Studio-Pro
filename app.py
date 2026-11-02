import streamlit as st

from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)



st.title("AI Content Generator Pro")

st.write("Welcome! Create business content with AI.")

topic = st.text_input("What topic do you want to write about?")
content_type = st.selectbox(
    "Choose content type:",
    ["Business Tips", "Instagram Caption", "Marketing Post", "Product Description"]
)

content_prompts = {
    "Business Tips": "Write exactly 3 practical business tips for beginners.",
    "Instagram Caption": "Write a short, engaging Instagram caption with a strong hook and relevant emojis.",
    "Marketing Post": "Write a persuasive marketing post with a strong hook and a clear call to action.",
    "Product Description": "Write a professional product description focusing on features and customer benefits."
}

language = st.selectbox(
    "choose content language ",
    ["English", "Arabic", "Kurdish (Sorani)"]
)

if st.button("Generate Content"):
    if topic.strip():
        with st.spinner("AI is generating content..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                                You are a professional business content creator.
                                Instructions: {content_prompts[content_type]}
                                Topic: {topic}

                                Write useful, engaging, and practical content.
                                Write the entire content in {language}.
                                Do not use any other language.
                                """
                    }
                ],
                temperature=0.7
            )

        st.subheader("Generated Content")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a topic.")