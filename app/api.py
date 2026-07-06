from fastapi import FastAPI
from app.models import ResumeRequest
from app.service import analyze_resume

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/analyze")
def analyze(request: ResumeRequest):
    """
    Analyzes a resume using the Gemini API and returns a ResumeAnalysis object.
    """
    result = analyze_resume(request.resume)
    return result
