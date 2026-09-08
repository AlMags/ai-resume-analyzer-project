from fastapi import APIRouter

from app.models.request_models import ResumeRequest
from app.models.response_models import ResumeAnalysis
from app.services.resume_service import analyze_resume_text

router = APIRouter()

@router.post(
    "/analyze", 
    response_model=ResumeAnalysis,
    summary="Analyze Resume",
    description="Analyze resume text using Google's Gemini API.",
)
def analyze(request: ResumeRequest):
    return analyze_resume_text(request.resume)
