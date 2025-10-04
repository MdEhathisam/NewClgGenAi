import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

myfile = st.file_uploader("Upload Images & Files")

question = st.text_input("Ask Anything")

if st.button("Send"):

    files = []

    if myfile is not None:

        file_bytes = myfile.read()

    if question is not None:

        st.text_input("")
        
    response = myaibot.models.generate_content(
               model="gemini-2.5-flash",
               contents = files
               )

    st.write(response.text)




