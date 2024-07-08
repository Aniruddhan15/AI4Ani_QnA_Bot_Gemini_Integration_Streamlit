from dotenv import load_dotenv
load_dotenv() 

import streamlit as st 
import os
import google.generativeai as genai 

genai.configure(api_key= os.getenv("g_api_key") )
model = genai.GenerativeModel("gemini-pro")

def get_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(layout="wide", page_title="Conversation App")

st.header(" Conversational QnA Web App based on Gemini LLM Application")
st.subheader("U get what you want!!")
input = st.text_input("Enter yor query")

submit = st.button("Click here for content generation")

if submit:
    response1 = get_response(input)
    st.subheader("Here is your desired response!") 
    st.write(response1)

