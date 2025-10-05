import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

myfiles = st.file_uploader("Upload Files", type=["jpeg","jpg","png","pdf","doc","docx"])

question = st.text_input("Ask Anything")

if st.button("Send"):
  if myfiles is not None:
    file_data = myfiles.read()

    model = myaibot.models.get("gemini-2.5-flash")
    response = model.generate_content(
    ,
    contents = [
        {  
          "role":"user","parts":[
                            {"text":question},
                            {"inline_data":{"mime_type":myfiles.type,"data":file_data}}
               ]
        }
      ]
    )

    st.write(response.text)
  else:
    
    st.write("Upload a file before sending")


