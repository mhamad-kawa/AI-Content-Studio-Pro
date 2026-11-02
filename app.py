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
                                Create content of this type: {content_type}
                                Topic: {topic}

                                Write useful, engaging, and practical content.
                                Use clear and simple English and arabic.
                                """
                    }
                ],
                temperature=0.7
            )

        st.subheader("Generated Content")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a topic.")