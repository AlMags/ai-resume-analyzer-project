import json
from app.models import ResumeAnalysis

def parse_response(response):

    cleaned = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        # remove json markdown
        data = json.loads(cleaned) # json.loads -> converts JSON string to Python dictionary
        return ResumeAnalysis(
            summary=data.get("summary", ""),
            skills=data.get("skills", []),
            years_experience=data.get("years_experience", ""),
            recommended_role=data.get("recommended_role", ""),
            score=data.get("score", 0)
        )
    except Exception as e:
        print(f"The model didn't return a valid JSON: {e}")