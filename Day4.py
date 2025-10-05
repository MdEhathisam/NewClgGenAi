
question = st.text_input("Ask Anything")

if st.button("Send"):
response = myaibot.models.generate_content(
model="gemini-2.5-flash",
contents = question
)

st.write(response.text)
