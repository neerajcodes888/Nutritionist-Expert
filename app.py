import gradio as gr
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API And get response
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, image[0], ""])
    return response.text

# Function to process uploaded image
def process_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        image_parts = [{"mime_type": uploaded_file.content_type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Gradio Interface
input_prompt = "You are an expert in nutritionist where you need to see the food items from the image and calculate the total calories, also provide the details of every food items with calories intake."

def predict(input_text, uploaded_file):
    image_data = process_image(uploaded_file)
    response = get_gemini_response(input_text, image_data)
    return response

image_input = gr.inputs.Image(label="Upload Image")
input_text = gr.inputs.Textbox(label="Input Prompt", placeholder="Enter prompt here...")
output_text = gr.outputs.Textbox(label="Total Calories")

gr.Interface(fn=predict, inputs=[input_text, image_input], outputs=output_text, title="Gemini Health App").launch()
