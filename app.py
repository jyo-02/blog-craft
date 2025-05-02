import streamlit as st
from langchain_utils import create_blog_chain

st.set_page_config(page_title="BlogCraft", layout="centered")
st.title("📚 BlogCraft: AI Blog Generator")

topic = st.text_input("Topic", "The future of AI in healthcare")
length = st.selectbox("Length", ["short", "medium", "long"])
tone = st.selectbox("Tone", ["informative", "casual", "professional", "humorous"])

length_map = {
    "short": "Keep the blog brief, around 300 words.",
    "medium": "Write a medium-length blog post with around 600-800 words.",
    "long": "Write an in-depth blog post with a detailed explanation, 900 words."
}

if st.button("Generate Blog"):
    chain = create_blog_chain()
    with st.spinner("Generating..."):
        try:
            prompt = f"Topic: {topic}. Tone: {tone}. {length_map[length]}"
            blog = chain.run(topic=topic, length=length, tone=tone, prompt=prompt)
            
            st.subheader("Generated Blog")
            st.write(blog)

        except Exception as e:
            st.error(f"Error generating blog: {e}")
