from fastapi import APIRouter, File, HTTPException, UploadFile

from app.file_extractor import extract_resume_text
from app.models.request_models import ResumeRequest
from app.models.response_models import ResumeAnalysis
from app.services.resume_service import analyze_resume_text

router = APIRouter()

MAX_UPLOAD_SIZE = 5 * 1024 * 1024  # 5 MB

@router.post(
    "/analyze", 
    response_model=ResumeAnalysis,
    summary="Analyze Resume",
    description="Analyze resume text using Google's Gemini API.",
)
def analyze(request: ResumeRequest):
    return analyze_resume_text(request.resume)

@router.post(
    "/analyze/upload",
    response_model=ResumeAnalysis,
    summary="Analyze an uploaded resume",
    description="Extract text from a PDF or TXT resume and analyze it."
)
def analyze_uploaded_resume(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="A file is required",
        )

    try:
        # Read at most 5 MB + 1 byte to detect overside uplaods
        content = file.file.read(MAX_UPLOAD_SIZE + 1)
    finally:
        file.file.close()

    if len(content) > MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=413,
            detail="The uploaded file exceeds the 5 MB limit.",
        )

    try:
        resume_text = extract_resume_text(file.filename, content)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    return analyze_resume_text(resume_text)