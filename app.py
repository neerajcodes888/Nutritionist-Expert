import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

from dotenv import load_dotenv

load_dotenv() 

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text