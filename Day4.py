import streamlit as st
from google import genai

# NOTE: For security, never hardcode API keys in production code. 
# Use st.secrets or environment variables.
myaibot = genai.Client(api_key="AIzaSyB1YeNps3ZNWaLJpGF4TpHPSGXJq1EMr3c")

st.title("My Own GPT")

# 1. Use columns to place the button-like element and the text input side-by-side.
# [1, 10] ratio keeps the button area small and the text input wide.
col1, col2 = st.columns([1, 10])

# --- Input Area Layout ---
with col1:
    # Option A: Use a simple button (less integrated look)
    # plus_button = st.button("➕", key="options_btn")
    
    # Option B: Use an Expander (More functional, though it expands *below* the button)
    # For a button-like appearance that triggers an action, a simple button (Option A) is better.
    # Let's stick with the request for a '+' button next to the input.
    plus_button = st.button("➕", key="options_btn", help="Click to open advanced options")
    

with col2:
    # Use label_visibility="collapsed" to remove the label above the input, 
    # making it align well with the button.
    question = st.text_input("Ask Anything", label_visibility="collapsed")

# --- Expandable Options ---
# The expander you want to show can be toggled based on the plus_button click.
if plus_button:
    # Alternatively, you can use the built-in expander and place it here 
    # to appear right below the input line.
    with st.expander("Advanced Options"):
        st.write("This section appears when the '+' button is clicked.")
        st.file_uploader("Upload context file (e.g., PDF, TXT)")
        st.slider("Creativity Level", 0.0, 1.0, 0.7)

# The original expander is separate and doesn't look like it's connected 
# to the text area, so we'll remove it from the final code:
# with st.expander("Click to expand"):
#     st.write("This content is hidden by default and expanded by '+' icon.")

# --- Send Button and Response ---
if st.button("Send"):
    # Check if the question is empty
    if not question:
        st.warning("Please ask a question!")
    else:
        # Generate content
        response = myaibot.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )
        st.write(response.text)
