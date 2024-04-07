# Nutritionist Expert 🥦🍔

## Table of Contents
- [Introduction](#introduction) 📝
- [Usage](#usage) 🚀
- [Deployed Application](#deployed-application) 🌐
- [Demo Video](#demo-video) ▶️
- [Installations](#installations) ⚙️
- [Google API Key](#google-api-key) 🔑
- [Running the Application](#running-the-application) ▶️
- [Tech Stack](#tech-stack) 💻
- [Benefits](#benefits) 🌟
- [Contributing](#contributing) 🤝
- [Credits](#credits) 🙌
- [License](#license) 📜

## Introduction 📝
Nutritionist Expert is an innovative application leveraging the power of Generative AI and Streamlit. It allows users to upload images of food for instant analysis of calorie content. Additionally, users can ask questions related to the uploaded image to gain deeper insights into the nutritional aspects of the food.

## Usage 🚀
To use Nutritionist Expert:
1. Upload an image of the food you want to analyze.
2. The application will provide information about the calorie content of the food.
3. Ask questions related to the uploaded image to learn more about its nutritional value.

## Deployed Application 🌐
[Link to Deployed Application]

## Demo Video ▶️
[Link to Demo Video]

## Installations ⚙️
To run Nutritionist Expert locally, ensure you have Python installed on your system. Clone the repository and install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Requirements
- streamlit
- google-generativeai
- python-dotenv
- langchain
- PyPDF2
- chromadb
- pdf2image
- faiss-cpu
- langchain_google_genai

## Google API Key 🔑
To use the Google API services, you need to obtain an API key from the Google Cloud Console and set it up in your environment. Create a .env file in the root directory of the project and add your API key as follows:

```bash
GOOGLE_API_KEY=your_api_key_here
```

## Running the Application ▶️
To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```
