from openai import OpenAI

from dotenv import load_dotenv

import os

load_dotenv()

key = os.getenv("SHARAD_RAJORE_KEY")  

client1 = OpenAI(api_key=key)  

client2 = OpenAI()  

          

response1 = client1.responses.create(
    model="gpt-4.1-mini",
    input="What is GenAI in simple terms in 2 lines"
)

response2 = client1.responses.create(
    model="gpt-4.1-mini",
    input="What is GenAI in simple terms"
)
print(response1.output_text)

print(response2.output_text)
