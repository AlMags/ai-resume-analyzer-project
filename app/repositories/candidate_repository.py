from app.clients.mongodb_client import get_database
from app.models.response_models import ResumeAnalysis


def save_analysis(analysis: ResumeAnalysis):
    db = get_database()
    collection = db["candidates"]

    document = {
        "summary": analysis.summary,
        "skills": analysis.skills,
        "years_experience": analysis.years_experience,
        "recommended_role": analysis.recommended_role,
        "score": analysis.score,
    }

    result = collection.insert_one(document)

    return result.inserted_id

def get_all_analyses(): 
    db = get_database