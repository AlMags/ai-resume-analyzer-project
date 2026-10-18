
from pathlib import Path

import app.api.analyze as analyze_api

from app.models.response_models import ResumeAnalysis

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"

# mock analyze_resume_text
def mock_analyze_resume_text(resume: str):
    # future test cases
    # mockResumes = [
    #     ResumeAnalysis(
    #         summary="Java Developer",
    #         skills=["Java", "Spring Boot"],
    #         years_experience="3",
    #         recommended_role="Backend Developer",
    #         score=92
    #     ),
    #     ResumeAnalysis(
    #         summary="Backend Developer",
    #         skills=["Python", "FastAPI"],
    #         years_experience="3",
    #         recommended_role="Backend Developer",
    #         score=90,
    #     )
    # ]
    
    return ResumeAnalysis(
        summary="Java Developer",
        skills=["Java", "Spring Boot"],
        years_experience="3",
        recommended_role="Backend Developer",
        score=92
    )

# /analyze
def test_analyze(client, monkeypatch):
    
    monkeypatch.setattr(
        analyze_api,
        "analyze_resume_text",
        mock_analyze_resume_text,
    )

    response = client.post(
        "/analyze",
        json={
            "resume": "Experienced Java Developer"
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert body["summary"] == "Java Developer"
    assert body["score"] == 92
    assert "Java" in body["skills"]

# mock analyze_uploaded_resume
def mock_analysis_service(monkeypatch):
    monkeypatch.setattr(
        analyze_api,
        "analyze_resume_text",
        mock_analyze_resume_text,
    )

# valid TXT upload
def test_analyze_uploaded_txt(client, monkeypatch):
    mock_analysis_service(monkeypatch)

    file_path = FIXTURES_DIR / "sample_resume.txt"

    with file_path.open("rb") as resume_file:
        response = client.post(
            "/analyze/upload",
            files={
                "file": (
                    "sample_resume.txt",
                    resume_file,
                    "text/plain",
                )
            },
        )

        assert response.status_code == 200

        body = response.json()
        assert body["summary"] == "Java Developer"
        assert "Java" in body["skills"]

def test_analyze_uploaded_pdf(client, monkeypatch):
    mock_analysis_service(monkeypatch)

    file_path = FIXTURES_DIR / "sample_resume.pdf"

    with file_path.open("rb") as resume_file:
        response = client.post(
            "/analyze/upload",
            files={
                "file": (
                    "sample_resume.pdf",
                    resume_file,
                    "application/pdf",
                )
            },
        )

        assert response.status_code == 200

        body = response.json()
        assert body["summary"] == "Java Developer"

def test_analyze_upload_unsupported_file(client, monkeypatch):
    mock_analysis_service(monkeypatch)

    response = client.post(
        "/analyze/upload",
        files={
            "file": (
                "sample_resume.docx",
                b"test content",
                "application/octet-stream",
            )
        },
    )

    assert response.status_code == 400
    assert "Unsupported file type" in response.json()["detail"]

def test_analyze_upload_empty_file(client, monkeypatch):
    mock_analysis_service(monkeypatch)

    response = client.post(
        "/analyze/upload",
        files={
            "file": (
                "sample_resume.txt",
                b"",
                "text/plain",
            )
        },
    )

    assert response.status_code == 400
    assert "empty" in response.json()["detail"].lower()

def test_analyze_upload_unreadable_pdf(client, monkeypatch):
    mock_analysis_service(monkeypatch)

    response = client.post(
        "/analyze/upload",
        files={
            "file": (
                "sample_resume.pdf",
                b"invalid pdf file",
                "application/pdf",
            )
        },
    )

    assert response.status_code == 400
    assert "The PDF file could not be read" in response.json()["detail"]

def test_analyze_upload_file_too_large(client, monkeypatch):
    mock_analysis_service(monkeypatch)

    oversized_content = b"a" * (5 * 1024 * 1024 + 1)

    response = client.post(
        "/analyze/upload",
        files={
            "file": (
                "large.txt",
                oversized_content,
                "text/plain",
            )
        },
    )

    assert response.status_code == 413
    assert "5 MB limit" in response.json()["detail"]
