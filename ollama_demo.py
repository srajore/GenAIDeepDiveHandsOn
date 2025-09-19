from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()


llm = ChatOllama(model="llama3.2:latest")

response = llm.invoke("What kind of applications I can develop using GenAI?")

print(response.content)