import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini_ideas(prompt):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Something went wrong: {e}"