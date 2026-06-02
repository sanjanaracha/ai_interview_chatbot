import streamlit as st
import requests

# server_url = st.secrets["backend_url"]

server_url = "https://127.0.0.1:8000"
st.title("AI Interview Chat Bot")

with st.form("Details"):

    Lang = st.text_input("Enter the Language")
    Topic = st.text_input("Enter the Topic")
    Level = st.selectbox("Enter the Level",["Easy", "Medium", "Advanced"])
    Type = st.multiselect("Enter the Type",["MCQ's", "Theory Questions", "Coding Snippets"])
    Submit_Button = st.form_submit_button("Submit")

    if Submit_Button:
        prompt = f"""
            Give me Questions in {Lang} Language on Topic Name is {Topic}
            in {Level} level and {Type} type.

            Follow:
            Do not give any explanation.
            Give only questions.
        """

        response = requests.post(f"{server_url}/questions",json={"prompt": prompt})
        data = response.json()
        if "response" in data:
            st.write(data["response"])
        else:
            st.error(data)