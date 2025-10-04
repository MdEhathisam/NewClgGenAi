import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

question = st.text_input("Ask Anything")

myfile = st.file_uploader("Upload Images & Files")

if st.button("Send"):
    response = myaibot.models.generate_content(
               model="gemini-2.5-flash",
               contents = [myfile,question]
               )

    st.write(response.text)
