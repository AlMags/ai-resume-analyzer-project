from fastapi.testclient import TestClient

from app.server import app
from app.api import candidates

client = TestClient(app)

def test_get_candidates(monkeypatch):
    expected_analyses = [
        {
            "_id": "test-id-1",
            "summary": "Test analysis",
            "skills": ["Python"],
            "years_experience": "1 year",
            "recommended_role": "Software Engineer",
            "score": 85,
        }
    ]

    def mock_retrieve_candidate_analyses():
        return expected_analyses

    monkeypatch.setattr(
        candidates,
        "retrieve_candidate_analyses",
        mock_retrieve_candidate_analyses,
    )

    response = client.get("/candidates")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "test-id-1",
            "summary": "Test analysis",
            "skills": ["Python"],
            "years_experience": "1 year",
            "recommended_role": "Software Engineer",
            "score": 85,
        }
    ]