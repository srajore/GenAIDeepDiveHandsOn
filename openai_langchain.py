from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

response = llm.invoke("What is GenAI in simple terms?")

print(response.content)