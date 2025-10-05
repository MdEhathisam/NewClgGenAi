import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

myimage = st.file_uploader("Upload Image", type=["jpeg","jpg","png"])

question = st.text_input("Ask Anything")

if st.button("Send"):
  if myimage is not None:
    response = myaibot.models.generate_content(
    model="gemini-2.5-flash",
    contents = [{"role":"user","parts":[{"text":question},{"inline_data":{"mime_type":myimage.type,"data":myimage.read()}}]}]
    )

    st.write(response.text)
  else:
    
    st.write("Upload an image before sending")



