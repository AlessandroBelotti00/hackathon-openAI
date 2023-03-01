import os
import streamlit as st
from openai_utils.openaiAPI import OpenAIAPI
from dotenv import load_dotenv
from api import call_api

load_dotenv()
OPENAI_KEY_VAR="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"
#os.getenv('openai_key')

## To be done: read from json/csv
subjects_list = ['English', 'Math', 'Science', 'Art', 'Lesson_Example']
st.title("Teacher AI")
st.markdown(
    "This mini-app generates elementary school lessons using OpenAI's GPT-3 based [Davinci model](https://beta.openai.com/docs/models/overview)."
)

col1, col2 = st.columns(2)

with col1:

    option = st.selectbox(
        'Select the subject',
        subjects_list)

    path = "../Example/" + option.lower() + "syllabus.txt"
    print(path)
    fileObject = open(path, "r")
    data = fileObject.read()

    pos = data.find("Week" ,0)
    for i in range(6):
        new_pos = data.find("Week" ,pos+3)
        st.write(data[pos:new_pos])
        oai = OpenAIAPI(OPENAI_KEY_VAR)
        st.write("EXPLANATION:\n", oai.call_API("explain me as a teacher in a complete form the concept of "+data[pos+7:new_pos]))
        pos = new_pos

        


with col2:
    gif_url = 'https://media.giphy.com/media/YT8NIA8fU2pz6Gf2kR/giphy.gif'
    st.image(gif_url, use_column_width=True)