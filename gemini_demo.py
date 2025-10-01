from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

prompt = ChatPromptTemplate.from_template(
    "Can you help with with the 4 key achivements of {name} in 50 words"
)


#prompt.format(name="Rahul Gandhi")


chain = prompt | llm   # LCEL 

st.title("Hello World")

st.header("This is a header")

user_name = st.text_input("Who's achivements would you like to know")

response = ""

if st.button("Click me"):
    with st.spinner("Generating response..."):
        response = chain.invoke({"name":user_name}).content

#result = (prompt | llm).invoke({"name":"Mahatma Gandhi"})   # LCEL 

#print(result.content)

st.write(response)

