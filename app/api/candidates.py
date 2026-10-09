from fastapi import APIRouter

from app.models.response_models import CandidateAnalysisResponse
from app.services.candidate_service import retrieve_candidate_analyses


router = APIRouter(tags=["Candidates"])

@router.get(
    "/candidates",
    response_model=list[CandidateAnalysisResponse],
    summary="Retrieve candidate analyses",
    description="Returns all saved candidate analyses.",
)
def get_candidates():
    analyses = retrieve_candidate_analyses()

    return [
        {
            "id": analysis["_id"],
            "summary": analysis["summary"],
            "skills": analysis["skills"],
            "years_experience": analysis["years_experience"],
            "recommended_role": analysis["recommended_role"],
            "score": analysis["score"]
        }
        for analysis in analyses
    ]
