from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to Gemini Pro Vision

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize streamlit app

st.set_page_config(page_title="Gemini Image")
st.header("Gemini Image Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If button is clicked

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)