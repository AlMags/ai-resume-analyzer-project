import pytest

from app.models.response_models import ResumeAnalysis
from app.services import resume_service


def test_analyze_resume_text(monkeypatch):
    expected_result = ResumeAnalysis(
        summary="Backend Developer",
        skills=["Python", "FastAPI"],
        years_experience="3",
        recommended_role="Backend Developer",
        score=90,
    )

    def mock_build_resume_prompt(resume_text):
        return "mock prompt"

    def mock_ask_gemini(prompt):
        return "mock response"

    def mock_parse_response(response):
        return expected_result

    monkeypatch.setattr(
        resume_service,
        "build_resume_prompt",
        mock_build_resume_prompt
    )

    monkeypatch.setattr(
        resume_service, 
        "ask_gemini",
        mock_ask_gemini,
    )

    monkeypatch.setattr(
        resume_service,
        "parse_response",
        mock_parse_response
    )

    result = resume_service.analyze_resume_text(
        "Experienced Python developer"
    )

    assert result == expected_result

def test_analyze_resume_text_failed_parsing_response(monkeypatch): 
    def mock_build_resume_prompt(resume_text):
            return "mock prompt"
    
    def mock_ask_gemini(prompt):
        return "mock response"

    monkeypatch.setattr(
        resume_service,
        "build_resume_prompt",
        mock_build_resume_prompt
    )

    monkeypatch.setattr(
        resume_service, 
        "ask_gemini",
        mock_ask_gemini,
    )

    monkeypatch.setattr(
        resume_service,
        "parse_response",
        lambda response: None,
    )

    with pytest.raises(
        RuntimeError,
        match="Failed to parse Gemini response."
    ):
        resume_service.analyze_resume_text(
            "Experienced Python developer"
        )