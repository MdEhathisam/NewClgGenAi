import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

myfile = st.file_uploader("Upload Images & Files")

question = st.text_input("Ask Anything")

if st.button("Send"):

    model="gemini-2.5-flash"

    if question:
        
        response = myaibot.models.generate_content(question)

        st.write(response.text)
    else:
        st.warning("Please enter a question")




