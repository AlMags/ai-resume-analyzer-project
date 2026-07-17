from app.prompt_builder import build_resume_prompt
from app.gemini_client import ask_gemini
from app.json_parser import parse_response
from app.models import ResumeAnalysis


def analyze_resume_text(resume_text: str) -> ResumeAnalysis:
    """
    Analyze a resume using Gemini and return a ResumeAnalysis object.
    """

    prompt = build_resume_prompt(resume_text)

    response = ask_gemini(prompt)

    result = parse_response(response)

    if result is None:
        raise RuntimeError("Failed to parse Gemini response.")

    return result