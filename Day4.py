import streamlit as st

from google import genai

from google.genai.types import Part

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

question = st.text_area("")

myfile = st.file_uploader("Upload Images & files")

mycamera = st.camera_input("Open Camera")

if st.button("Send"):

    files = []

    if question:

        files.append("Ask Anything")

    if myfile is not None:
    
        file_bytes = myfile.read()
        
        files.append(myfile.type,file_bytes)
    
    if mycamera is not None:
    
        camera_bytes = mycamera.getvalue()
        
        files.append(camera_bytes)
    
    response = myaibot.models.generate_content(
               model="gemini-1.5-flash",
               contents = files
               )
    
    st.write(response.text)











