import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

col1,col2 = st.columns([4,1])

with col1:
    question = st.text_input("Ask Anything", height = 100, lable_visibility = "collapsed")

with col2:
    add_button = st.button("+",use_container_width = True)

send_button = st.button("Send")

if send_button:

    contents = [question]
    response = myaibot.models.generate_content(
               model="gemini-2.5-flash",
               contents = contents
               )

    st.write(response.text)








