
import streamlit as st

from groq import Groq

# -------------------------------
# 1. Connect to Groq
# -------------------------------

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# -------------------------------
# 2. Initialize Session State
# -------------------------------

if "content_history" not in st.session_state:
    st.session_state.content_history = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "generated_content" not in st.session_state:
    st.session_state.generated_content = ""

# -------------------------------
# 3. App Title
# -------------------------------

st.title("AI Content Generator Pro")

st.write("Welcome! Create business content with AI.")

# -------------------------------
# 4. User Inputs
# -------------------------------

topic = st.text_input(
    "What topic do you want to write about?"
)

content_type = st.sidebar.selectbox(
    "Choose content type:",
    [
        "Business Tips",
        "Instagram Caption",
        "Marketing Post",
        "Product Description"
    ]
)

content_length = st.sidebar.selectbox(
    "Choose Content Length:",
    ["Short", "Medium", "Long"]
)

brand_name = st.text_input(
    "Brand Name:",
    placeholder="Enter your company name..."
)

brand_description = st.text_area(
    "Describe your brand:",
    placeholder="Tell us about your company, products, services, and customers..."
)

custom_instructions = st.text_area(
    "Custom Instructions:",
    placeholder="Tell AI how you want your content to be written..."
)

content_prompts = {
    "Business Tips": "Write exactly 3 practical business tips for beginners.",
    "Instagram Caption": "Write a short, engaging Instagram caption with a strong hook and relevant emojis.",
    "Marketing Post": "Write a persuasive marketing post with a strong hook and a clear call to action.",
    "Product Description": "Write a professional product description focusing on features and customer benefits."
}

language = st.sidebar.selectbox(
    "Choose content language:",
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

# -------------------------------
# 5. Generate Content
# -------------------------------

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
Content Length: {content_length}
Target Audience: {audience}
Brand Voice: {brand_voice}
Brand Name: {brand_name}
Brand Description: {brand_description}
Custom Instructions: {custom_instructions}
Topic: {topic}

Write useful, engaging, and practical content.

Do not invent facts, prices, discounts, warranties,
return policies, product features, or customer testimonials.

Use the Brand Description as the only source of factual
information about the brand and its products.

Use the Topic only to understand the content idea,
not as a source of factual claims.

Do not include any claims from the Topic unless
they are confirmed in the Brand Description.

If a fact is missing from the Brand Description,
do not mention it.

Write the entire content in {language}.
Do not use any other language.
"""
                    }
                ],
                temperature=creativity
            )

        generated_content = response.choices[0].message.content

        st.session_state.generated_content = generated_content

        st.session_state.content_history.append(
            generated_content
        )

    else:
        st.warning("Please enter a topic.")

# -------------------------------
# 6. Display Generated Content
# -------------------------------

if st.session_state.generated_content:

    st.subheader("Generated Content")

    st.code(
        st.session_state.generated_content,
        language=None
    )

    if st.button("⭐ Save to Favorites"):

        if st.session_state.generated_content not in st.session_state.favorites:

            st.session_state.favorites.append(
                st.session_state.generated_content
            )

            st.success("Content saved to favorites!")

        else:
            st.info("This content is already in your favorites.")

    st.download_button(
        label="Download Content",
        data=st.session_state.generated_content,
        file_name="ai_content.txt",
        mime="text/plain"
    )

# -------------------------------
# 7. Content History
# -------------------------------

st.subheader("Content History")

if st.button("Clear History"):
    st.session_state.content_history = []

for content in st.session_state.content_history:

    st.write(content)

    st.divider()

# -------------------------------
# 8. Favorite Content
# -------------------------------

st.subheader("⭐ Favorite Content")

if st.button("Clear Favorites"):
    st.session_state.favorites = []

if st.session_state.favorites:

    for index, content in enumerate(st.session_state.favorites):

        st.write(content)

        st.divider()

else:
    st.info("No favorite content saved yet.")
