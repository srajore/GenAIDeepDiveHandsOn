from openai import OpenAI

client = OpenAI(api_key="")

response = client.responses.create(
    model="gpt-4.1-mini",
    input="What is GenAI in simple terms in 2 lines"
)

print(response.output_text)
