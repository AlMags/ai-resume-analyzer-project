import app.api.analyze as analyze_api

from app.models.response_models import ResumeAnalysis

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