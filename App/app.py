import streamlit as st


st.title("Teacher AI")
st.markdown(
    "This mini-app generates elementary school lessons using OpenAI's GPT-3 based [Davinci model](https://beta.openai.com/docs/models/overview)."
)
fileObject = open("../Example/lesson_example.txt", "r")
data = fileObject.read()

option = st.selectbox(
    'Select the subject',
    ('English', 'Math', 'Science'))


if option == 'Math':
    st.write('You selected:', data)