from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

import os

key = os.getenv("hf_api_token")

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    huggingfacehub_api_token=key
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("How I can learn GenAI quickly in 2 lines?")

print(response.content)