import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

myfiles = st.file_uploader("Upload Files", type=["jpeg","jpg","png","pdf","txt","mkv","mp4","mp3"])

myfilesread = myfiles

question = st.text_input("Ask Anything")

if st.button("Send"):
  if myfiles is not None:
    file_data = myfiles.read()

    response = myaibot.models.generate_content(
            model="gemini-2.5-flash",
            contents = [
              {  
                    "role":"user",
                    "parts":[
                        {"text":question},
                        {"inline_data":{"mime_type":myfilesread.type,"data":file_data}}
               ]
              }
      ]
    )

    st.write(response.text)
  else:
    
    st.write("Upload a file before sending")


