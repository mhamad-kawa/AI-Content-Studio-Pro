import streamlit as st

from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)



st.title("AI Content Generator Pro")

st.write("Welcome! Create business content with AI.")

topic = st.text_input("What topic do you want to write about?")

if st.button("Generate Content"):
    if topic.strip():
        with st.spinner("AI is generating content..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": f"Write 3 practical business tips for beginners about: {topic}"
                    }
                ],
                temperature=0.7
            )

        st.subheader("Generated Content")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a topic.")