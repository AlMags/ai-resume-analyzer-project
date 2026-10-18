
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader


SUPPORTED_EXTENSIONS = {".pdf", ".txt"}

def extract_resume_text(filename: str, content: bytes) -> str:
    """Extract resume text from supported PDF or TXT files"""

    extension = Path(filename).suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError("Unsupported file type. Upload a PDF or TXT file")

    if not content: 
        raise ValueError("The uploaded file is empty")

    if extension == ".txt":
        try:
            text = content.decode("utf-8-sig")
        except UnicodeDecodeError as exc:
            raise ValueError(
                "The TXT file must contain valid UTF-8 text"
            ) from exc
    else:
        try: 
            reader = PdfReader(BytesIO(content))
            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )
        except Exception as exc:
            raise ValueError(
                "The PDF file could not be read"
            ) from exc

    text = text.strip()

    if not text:
        raise ValueError("No extractable text was found in the file")

    return text