# prompts.py
from langchain import PromptTemplate

# Template for blog generation with placeholders
BLOG_TEMPLATE = """
Write a {length} blog post about "{topic}" in a {tone} tone.
Include an introduction, main content, and conclusion.
"""

def get_blog_prompt() -> PromptTemplate:
    """
    Returns a PromptTemplate configured for blog generation.
    """
    return PromptTemplate(
        input_variables=["topic", "length", "tone"],
        template=BLOG_TEMPLATE
    )