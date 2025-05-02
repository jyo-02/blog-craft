# langchain_utils.py
import os
from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from prompts import get_blog_prompt
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
HUGGINGFACE_MODEL = os.getenv("HUGGINGFACE_MODEL", "meta-llama/Llama-2-7b-instruct-hf")
HUGGINGFACE_ENDPOINT_URL = os.getenv(
    "HUGGINGFACE_ENDPOINT_URL",
    f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL}"
)

def create_blog_chain():
    """
    Constructs an LLMChain using HuggingFaceEndpoint for blog generation.
    """
    llm = HuggingFaceEndpoint(
        endpoint_url=HUGGINGFACE_ENDPOINT_URL,
        huggingfacehub_api_token=HUGGINGFACE_TOKEN,
        temperature=0.7,
        max_new_tokens=512,
    )
    prompt = get_blog_prompt()
    return LLMChain(llm=llm, prompt=prompt)