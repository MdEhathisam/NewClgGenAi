import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

question = st.text_area("Ask Anything")

if myfile is not None:

    myfile = st.file_uploader("Upload Images & files")

    file_bytes = myfile.read()

if mycamera is not None:

    mycamera = st.camera_input("Open Camera")

    camera_ bytes = mycamera.getvalue()


#mycamera = st.camera_input("Open Camera")

if st.button("Send"):
    response = myaibot.models.generate_content(
               model="gemini-1.5-flash",
               contents = [question,file_bytes]
               )

    st.write(response.text)







