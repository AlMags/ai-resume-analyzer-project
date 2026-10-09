from app.repositories import candidate_repository


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
        candidate_repository,
        "get_database",
        mock_get_database,
    )

    analysis = candidate_repository.ResumeAnalysis(
        summary="Test summary",
        skills=["Python", "React"],
        years_experience="2 years",
        recommended_role="Software Engineer",
        score=85
    )

    result = candidate_repository.save_analysis(analysis)

    assert result is mock_inserted_id


def test_get_all_analyses(monkeypatch):
    mock_documents = [
        {
            "_id": "test-id-1",
            "summary": "First analysis",
            "skills": ["Python"],
            "years_experience": "1 year",
            "recommended_role": "Junior Developer",
            "score": 75,
        },
        {
            "_id": "test-id-2",
            "summary": "Second analysis",
            "skills": ["React"],
            "years_experience": "2 years",
            "recommended_role": "Frontend Developer",
            "score": 85,
        },
    ]

    class MockCollection:
        def find():
            return mock_documents

    class MockDatabase:
        def __getitem__(self, name):
            assert name == "candidates"
            return MockCollection

    def mock_get_database():
        return MockDatabase()

    monkeypatch.setattr(
        candidate_repository,
        "get_database",
        mock_get_database
    )

    result = candidate_repository.get_all_analyses()

    assert len(result) > 0
    assert result[0]["summary"] == "First analysis"
    assert result[1]["summary"] == "Second analysis"
    assert result[0]["_id"] == "test-id-1"
    assert result[1]["_id"] == "test-id-2"