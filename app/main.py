import os
import json
from google import genai
from dotenv import load_dotenv
from app.prompt_builder import build_resume_prompt
from app.gemini_client import ask_gemini
from app.json_parser import parse_response
from app.save_candidate import save_candidate

# from google import genai -> imports Google's AI Library
# from dotenv import load_dotenv -> allows python to read your .env file
# import os -> allows python to interact with your operating system, including reading environment variables
# import json -> to process json returned by your prompts

load_dotenv() # loads your .env file

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
    # gets the value of GEMINI_API_KEY from your .env file and returns it
    # then creates an object that knows how to talk to Gemini i.e. "client"
)

print("Reading resume...")

with open("resume.txt", "r", encoding="utf-8") as file:
    resume = file.read()

# open -> opens the file
# "r" -> read-only, other modes: w-"write" and a-"append"
# "utf-8" -> tells python how to interpret the text
# file.read -> uses your file variable and reads the entire file i.e. resume.txt

# print(resume) -> verify if the resume.txt is read

prompt = build_resume_prompt(resume)

print("Sending to Gemini...\n\n")

response = ask_gemini(prompt)

print("Processing...\n\n")

result = parse_response(response)

print("Done!\n\n")

if result.score >= 80:
    save_candidate("interview.txt", result)
else:
    save_candidate("review.txt", result)

print("====Credentials====\n\n")
print("===================\n\n")
print(f"{result.summary}\n\n")
print(f"{result.skills}\n\n")
print(f"{result.years_experience}\n\n")
print(f"{result.recommended_role}\n\n")
print(f"{result.score}\n\n")