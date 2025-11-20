import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

#Chat History Setup

if "messages" not in st.session_state:

    st.session_state.messages = []   
# Display chat history

for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.chat_message("user").markdown(msg["content"])

    else:

        st.chat_message("assistant").markdown(msg["content"])


question = st.text_input("Ask Anything")

if question:

    # Save user message

    st.session_state.messages.append({"role": "user", "content": question})

    st.chat_message("user").markdown(question)

    # Send request to AI model

    response = myaibot.models.generate_content(

        model="gemini-2.5-flash",

        contents=question

    )

    ai_reply = response.text

    # Save bot message

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    st.chat_message("assistant").markdown(ai_reply)




