from app.repositories.candidate_repository import get_all_analyses


def retrieve_candidate_analyses():
    """
    Retrieve all saved candidate analyses.
    """
    return get_all_analyses()