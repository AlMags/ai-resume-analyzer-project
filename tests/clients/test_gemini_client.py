from app.clients import gemini_client


def test_get_client(monkeypatch):
    mock_client = ()

    def mock_get_gemini_api_key():
        return "test-api-key"

    monkeypatch.setattr(
        gemini_client,
        "get_gemini_api_key",
        mock_get_gemini_api_key,
    )

    def mock_genai_client(api_key):
        assert api_key == "test-api-key"
        return mock_client

    monkeypatch.setattr(
        gemini_client.genai,
        "Client",
        mock_genai_client,
    )

    result = gemini_client.get_client()

    assert result is mock_client


def test_ask_gemini(monkeypatch):
    # mock your LLM version
    class MockModels:
        # mock of generate_content method
        def generate_content(model, contents):
            assert model == "gemini-2.5-flash"
            assert contents == "test prompt"

            class MockResponse:
                text = "Gemini response"

            return MockResponse

    class MockClient:
        models = MockModels

    monkeypatch.setattr(
        gemini_client,
        "get_client",
        lambda: MockClient(),
    )

    result = gemini_client.ask_gemini("test prompt")

    assert result == "Gemini response"


    