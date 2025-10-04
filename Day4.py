import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

question = st.text_area("Ask Anything")

myfile = st.file.uploader("Upload Images & files")

mycamera = st.camera_input("Open Camera")

if st.button("Send"):
    response = myaibot.models.generate_content(
               model="gemini-2.5-flash",
               contents = [question,myfile,mycamera]
               )

    st.write(response.text)


