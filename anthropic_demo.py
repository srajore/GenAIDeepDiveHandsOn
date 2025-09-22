from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model='claude-3-opus-20240229')

response = llm.invoke("What kind of applications I can develop using GenAI?")

print(response.content)