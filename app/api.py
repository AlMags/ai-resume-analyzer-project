from fastapi import FastAPI
from app.models import ResumeRequest
from app.models import ResumeAnalysis
from app.service import analyze_resume

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/analyze", response_model=ResumeAnalysis)
def analyze(request: ResumeRequest):
    """
    Analyzes a resume using the Gemini API and returns a ResumeAnalysis object.
    """
    return analyze_resume(request.resume)
