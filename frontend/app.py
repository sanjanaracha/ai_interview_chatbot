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
        if "MCQ's" in Type:
            prompt += """
            - Generate 5 MCQ questions.
            - Provide 4 options (A, B, C, D).
            - Mention the correct answer.
            """

        if "Theory Questions" in Type:
            prompt += """
            - Generate 5 theory/interview questions.
            - Provide concise and accurate answers.
            """

        if "Coding Snippets" in Type:
            prompt += """
            - Generate 3 coding questions.
            - Provide complete code solutions.
            - Briefly explain the logic.
            """

            prompt += """
            Do not generate any question types that were not selected.
            Format the response neatly with headings for each selected section.
            """
        response = requests.post(f"{server_url}/questions",json={"prompt": prompt})
        data = response.json()
        if "response" in data:
            st.write(data["response"])
        else:
            st.error(data)
