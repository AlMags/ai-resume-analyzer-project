
import os

from dotenv import load_dotenv

load_dotenv()

def get_gemini_api_key():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY environment variable is missing."
        )

    return api_key

def get_mongodb_uri():
    uri = os.getenv("MONGODB_URI")

    if not uri:
        raise RuntimeError(
            "MONGODB_URI environment variable is missing."
        )

    return uri

def get_mongodb_database():
    database = os.getenv("MONGODB_DATABASE")

    if not database:
        raise RuntimeError(
            "MONGODB_DATABASE environment variable is missing."
        )

    return database