from app.repositories import save_analysis


def test_save_candidate(monkeypatch):
    mock_inserted_id = object()

    class MockCollection:
        def insert_one(document):
            assert document == {
                "summary": "Test summary",
                "skills": ["Python", "React"],
                "years_experience": "2 years",
                "recommended_role": "Software Engineer",
                "score": 85,
            }

            class MockResult:
                inserted_id = mock_inserted_id

            return MockResult()

    class MockDatabase:
        def __getitem__(self, name):
            assert name == "candidates"
            return MockCollection

    def mock_get_database():
        return MockDatabase()

    monkeypatch.setattr(
        save_analysis,
        "get_database",
        mock_get_database,
    )

    analysis = save_analysis.ResumeAnalysis(
        summary="Test summary",
        skills=["Python", "React"],
        years_experience="2 years",
        recommended_role="Software Engineer",
        score=85
    )

    result = save_analysis.save_analysis(analysis)

    assert result is mock_inserted_id