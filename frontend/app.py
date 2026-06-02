import streamlit as st
import requests

server_url = st.secrets["be_url"]
st.title("AI Interview Chat Bot")

with st.form("Details"):

    Lang = st.text_input("Enter the Language")
    Topic = st.text_input("Enter the Topic")
    Level = st.selectbox("Enter the Level",["Easy", "Medium", "Advanced"])
    Type = st.multiselect("Enter the Type",["MCQ's", "Theory Questions", "Coding Snippets"])
    Submit_Button = st.form_submit_button("Submit")

    if Submit_Button:
        prompt = f"""
        Act as an expert technical interviewer.

        Generate {Level} level interview questions for:

        Programming Language: {Lang}
        Topic: {Topic}
        Selected Types: {', '.join(Type)}

        Rules:

        - For MCQ's:
        * Generate 5 MCQs.
        * Include 4 options.
        * Mention the correct answer.

        - For Theory Questions:
        * Generate 5 interview questions.
        * Provide clear answers.

        - For Coding Snippets:
        * Generate 3 coding questions.
        * Provide complete code solutions.
        * Explain the logic briefly.

        Format the response neatly using headings:
        ## MCQ's
        ## Theory Questions
        ## Coding Snippets

        Generate only the sections corresponding to the selected types.
        """

        response = requests.post(f"{server_url}/questions",json={"prompt": prompt})
        data = response.json()
        if "response" in data:
            st.write(data["response"])
        else:
            st.error(data)
