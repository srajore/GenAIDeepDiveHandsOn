from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
# pip install torch
# pip install python-certifi-win32
# pip install transformers
import os

os.environ["HF_HOME"] = "D:\huggingface_cache"

key = os.getenv("hf_api_token")

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    #huggingfacehub_api_token=key
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("How I can learn GenAI quickly in 2 lines?")

print(response.content)