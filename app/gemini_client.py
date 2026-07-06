# this is where we talk to Gemini
from google import genai
from dotenv import load_dotenv
import os

load_dotenv() # loads your .env file

def get_client():
    # gets the value of GEMINI_API_KEY from your .env file and returns it
    # then creates an object that knows how to talk to Gemini i.e. "client"
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(prompt):
    client = get_client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text