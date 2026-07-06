from app.prompt_builder import build_resume_prompt
from app.gemini_client import ask_gemini
from app.json_parser import parse_response

def analyze_resume(resume_text: str):
    """
    Analyzes a resume using the Gemini API and returns a ResumeAnalysis object.
    """

    prompt = build_resume_prompt(resume_text)
    
    response = ask_gemini(prompt)

    result = parse_response(response)

    return result