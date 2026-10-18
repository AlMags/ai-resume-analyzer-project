from types import SimpleNamespace

import pytest

from app import file_extractor
from app.file_extractor import extract_resume_text


def text_extract_txt_text():
    result = extract_resume_text(
        "resume.txt",
        b"  Software Engineer with Python experience."
    )

    assert result == "Software Engineer with Python experience."

def test_extract_txt_with_utf8_bom():
    result = extract_resume_text(
        "resume.txt",
        b"\xef\xbb\xbfResume content",
    )

    assert result == "Resume content"

def test_extract_pdf_text(monkeypatch):
    mock_reader = SimpleNamespace(
        pages=[
            SimpleNamespace(
                extract_text=lambda: "Software Engineer"
            ),
            SimpleNamespace(
                extract_text=lambda: "Python Developer"
            ),
        ]
    )

    monkeypatch.setattr(
        file_extractor,
        "PdfReader",
        lambda stream: mock_reader,
    )

    result = extract_resume_text("resume.pdf", b"mock pdf bytes")

    assert result == "Software Engineer\nPython Developer"

def test_reject_unsupported_file_type():
    with pytest.raises(ValueError, match="Unsupported file type"):
        extract_resume_text("resume.docx", b"resume content")

def test_reject_empty_file():
    with pytest.raises(ValueError, match="The uploaded file is empty"):
        extract_resume_text("resume.txt", b"")

def test_reject_invalid_utf8():
    with pytest.raises(ValueError, match="The TXT file must contain valid UTF-8 text"):
        extract_resume_text("resume.txt", b"\xff\xfe\xfa")

def test_reject_pdf_without_extractable_text(monkeypatch):
    mock_reader = SimpleNamespace(
        pages=[
            SimpleNamespace(extract_text=lambda: None),
        ]
    )

    monkeypatch.setattr(
        file_extractor,
        "PdfReader",
        lambda stream: mock_reader,
    )

    with pytest.raises(ValueError, match="No extractable text"):
        extract_resume_text("resume.pdf", b"mock pdf bytes")

