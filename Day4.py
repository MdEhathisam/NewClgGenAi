import streamlit as st

from google import genai

myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

st.markdown("""
    <style>
    .textarea-container {
        position: relative;
        width: 100%;
    }
    textarea {
        width: 100% !important;
        padding-right: 40px !important; /* space for button */
    }
    .plus-button {
        position: absolute;
        right: 10px;
        bottom: 10px;
        background-color: #0d6efd;
        color: white;
        border: none;
        border-radius: 5px;
        width: 30px;
        height: 30px;
        cursor: pointer;
    }
    </style>
    <div class="textarea-container">
        <textarea id="custom-textarea" rows="4"></textarea>
        <button class="plus-button" onclick="alert('Plus clicked!')">+</button>
    </div>
""", unsafe_allow_html=True)

#col1,col2 = st.columns([5, 1])

#with col1:
 #   question = st.text_area("Ask Anything", height = 10, label_visibility = "collapsed")

#with col2:
 #   st.write("")
  #  st.write("")
   # add_button = st.button("+",use_container_width = True)

send_button = st.button("Send")

if send_button:

    st.warning("⚠️ Custom HTML textarea does not return value directly. Use st.text_area for backend logic.")

    #contents = [question]
    #if add_button:
     #   contents.append("You clicked the + button!")
    #response = myaibot.models.generate_content(
               model="gemini-2.5-flash",
               contents = contents
               )

    #st.write(response.text)



















