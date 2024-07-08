from dotenv import load_dotenv
load_dotenv() 

import streamlit as st 
import os
import google.generativeai as genai 
from PIL import Image
genai.configure(api_key= os.getenv("g_api_key") )
model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input, image):
    if input !="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(layout="wide", page_title="Conversation App")

st.header(" Conversational Image Generator App")
st.subheader(" Get Crazy pcitures u would have never dreamt of!!!")
input = st.text_input("Enter yor query", key="input")
 
upload = st.file_uploader("Select an Image from your device", type=['jpg','png','mp4'])
image=""
if upload is not None:
    image = Image.open(upload)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    
submit = st.button("Click here for your Desired Image")

if submit:
    response1 = get_response(input,image)
    st.subheader("Here is your desired response!") 
    st.write(response1)

