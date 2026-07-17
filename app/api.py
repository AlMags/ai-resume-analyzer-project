from fastapi import FastAPI

from app.models.request_models import ResumeRequest
from app.models.response_models import ResumeAnalysis
from app.services.resume_service import analyze_resume_text

app = FastAPI(
    title="AI Resume Analyzer API",
    version="0.1.0",
)


@app.get(
    "/health",
    summary="Health Check",
    description="Returns the current health status of the API",
)
def health():
    return {"status": "healthy"}


@app.post(
    "/analyze", 
    response_model=ResumeAnalysis,
    summary="Analyze Resume",
    description="Analyze resume text using Google's Gemini API.",
)
def analyze(request: ResumeRequest):
    try:
        return analyze_resume_text(request.resume)
    except RuneTimeError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )