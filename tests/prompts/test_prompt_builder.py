from app.json_parser import parse_response


def test_valid_json():
    mock_response = """
    {
        "summary": "Java Developer",
        "skills": ["Java"]
    }
    """

    result = parse_response(mock_response)

    assert result.summary == "Java Developer"

def test_invalid_json():
    mock_response = "test"

    result = parse_response(mock_response)

    assert result is None