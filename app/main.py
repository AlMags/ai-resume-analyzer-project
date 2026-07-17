import os
from dotenv import load_dotenv

from app.services.resume_service import analyze_resume_text
from app.candidate_storage import candidate_storage

load_dotenv()


def main():

    print("Reading resume...")

    resume_path = os.path.join("data", "resume.txt")

    with open(resume_path, "r", encoding="utf-8") as file:
        resume = file.read()

    print("Analyzing resume...\n")

    result = analyze_resume_text(resume)

    print("Analysis complete.\n")

    if result.score >= 80:
        candidate_storage("interview.txt", result)
    else:
        candidate_storage("review.txt", result)

    print("===== Resume Analysis =====\n")

    print(f"Summary: {result.summary}")
    print(f"Skills: {result.skills}")
    print(f"Experience: {result.years_experience}")
    print(f"Recommended Role: {result.recommended_role}")
    print(f"Score: {result.score}")


if __name__ == "__main__":
    main()