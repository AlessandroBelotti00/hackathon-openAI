import os
import streamlit as st
from openai_utils.openaiAPI import OpenAIAPI
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY_VAR=os.getenv('openai_key')

## To be done: read from json/csv
subjects_list = ['English', 'Math', 'Science']


st.title("Teacher AI")
st.markdown(
    "This mini-app generates elementary school lessons using OpenAI's GPT-3 based [Davinci model](https://beta.openai.com/docs/models/overview)."
)

fileObject = open("Example/lesson_example.txt", "r")
data = fileObject.read()

option = st.selectbox(
    'Select the subject',
    subjects_list)


if option == 'Math':
    st.write('You selected:', data)


text_input = st.text_input(
    "GPT3 text 👇",
 #   label_visibility=st.session_state.visibility,
 #   disabled=st.session_state.disabled,
 #   placeholder=st.session_state.placeholder,
)
if text_input:
    oai = OpenAIAPI(OPENAI_KEY_VAR)
    st.write("Answer\n", oai.call_API(text_input))