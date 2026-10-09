from app.services import candidate_service


def test_retrieve_candidate_analyses(monkeypatch):
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

    def mock_get_all_analyses():
        return expected_analyses

    monkeypatch.setattr(
        candidate_service,
        "get_all_analyses",
        mock_get_all_analyses,
    )

    result = candidate_service.retrieve_candidate_analyses()

    assert result == expected_analyses