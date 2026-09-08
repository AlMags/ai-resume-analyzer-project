
import os

from dotenv import load_dotenv

load_dotenv()

def get_gemini_api_key():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY environment variable is required."
        )

    return api_key