import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_ideas(user_input):
    prompt = f"Suggest 3 innovative hackathon project ideas based on this: {user_input}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're an expert at brainstorming cool tech ideas."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.8,
    )

    return response.choices[0].message["content"]
