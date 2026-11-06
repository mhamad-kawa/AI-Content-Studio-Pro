import streamlit as st

from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)



st.title("AI Content Generator Pro")

st.write("Welcome! Create business content with AI.")
if "content_history" not in st.session_state:
    st.session_state.content_history = []

topic = st.text_input("What topic do you want to write about?")
content_type = st.sidebar.selectbox(
    "Choose content type:",
    ["Business Tips", "Instagram Caption", "Marketing Post", "Product Description"]
)

content_prompts = {
    "Business Tips": "Write exactly 3 practical business tips for beginners.",
    "Instagram Caption": "Write a short, engaging Instagram caption with a strong hook and relevant emojis.",
    "Marketing Post": "Write a persuasive marketing post with a strong hook and a clear call to action.",
    "Product Description": "Write a professional product description focusing on features and customer benefits."
}

language = st.sidebar.selectbox(
    "choose content language ",
    ["English", "Arabic", "Kurdish (Sorani)"]
)

tone = st.sidebar.selectbox(
    "Choose writing tone:",
    ["Professional", "Friendly", "Persuasive", "Motivational"]
)

creativity = st.sidebar.slider(
    "Creativity Level:",
    min_value=0.2,
    max_value=1.0,
    value=0.7,
    step=0.1
)

audience = st.sidebar.selectbox(
    "Choose target audience:",
    ["Entrepreneurs", "Students", "Business Owners", "Beginners"]
)


brand_voice = st.sidebar.selectbox(
    "Choose Brand Voice:",
    ["Friendly", "Professional", "Casual", "Luxury"]
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
                                Writing Tone: {tone}
                                Target Audience: {audience}
                                Brand Voice: {brand_voice}
                                Topic: {topic}

                                Write useful, engaging, and practical content.
                                Write the entire content in {language}.
                                Do not use any other language.
                                """
                    }
                ],
                temperature=creativity
            )

        generated_content = response.choices[0].message.content
        st.session_state.content_history.append(generated_content)
        st.subheader("Generated Content")
        st.code(generated_content, language=None)
        st.download_button(
            label = "Download Content",
            data= generated_content , 
            file_name= "ai_content.txt" ,
            mime= "text/plain"
        )

    else:
        st.warning("Please enter a topic.")

st.subheader("Content History")
if st.button("Clear History"):
    st.session_state.content_history = []



for content in st.session_state.content_history:
    st.write(content)
    st.divider()