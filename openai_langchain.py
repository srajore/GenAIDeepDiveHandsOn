from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(max_tokens=100)

response = llm.invoke("What is GenAI ?")

print(response.content)