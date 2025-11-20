import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

if "messages" not in st.session_state:
    st.session_state.messages = []
question = st.text_input("Ask Anything")

if st.button("Send") and question:
       st.session_state.messages.append({"role":"user","content": question})
       
       response = myaibot.models.generate_content(
       
       model="gemini-2.5-flash",
  
       contents = st.session_state.messages
  )
st.session_state.messages.append({"role": "assistant",
                                  "content": response.text})
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


  #st.write(response.text)




