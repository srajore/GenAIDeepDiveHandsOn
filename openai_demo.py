from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="What is GenAI in simple terms in 2 lines"
)

print(response.output_text)
