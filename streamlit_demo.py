import streamlit as st

st.title("Hello World")

st.header("This is a header")

st.text("This is a text")

user_name = st.text_input("Enter your name")

print(user_name)

st.button("Click me")


