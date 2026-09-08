from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/health",
    summary="Health Check",
    description="Returns the current health status of the API",
)
def health():
    return {"status": "healthy"}