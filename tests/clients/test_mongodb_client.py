from app.clients import mongodb_client


def test_get_client(monkeypatch):
    mock_client = object()

    def mock_get_mongodb_uri():
        return "test-uri"

    def mock_mongodb_client(uri):
        assert uri == "test-uri"
        return mock_client

    monkeypatch.setattr(
        mongodb_client,
        "get_mongodb_uri",
        mock_get_mongodb_uri,
    )

    monkeypatch.setattr(
        mongodb_client,
        "MongoClient",
        mock_mongodb_client,
    )

    result = mongodb_client.get_client()

    assert result is mock_client

def test_get_database(monkeypatch):
    mock_database = object()

    class MockClient:
        def __getitem__(self, name):
            assert name == "test-item"
            return mock_database

    def mock_get_client():
        return MockClient()

    def mock_get_mongodb_database():
        return "test-item"

    monkeypatch.setattr(
        mongodb_client,
        "get_client",
        mock_get_client,
    )

    monkeypatch.setattr(
        mongodb_client,
        "get_mongodb_database",
        mock_get_mongodb_database,
    )

    result = mongodb_client.get_database()

    assert result is mock_database