from dataclasses import dataclass
from pydantic import BaseModel

class ResumeRequest(BaseModel):
    resume: str
@dataclass # generates the helpers and other methods that you may need for a python class
class ResumeAnalysis:
    summary: str
    skills: list[str]
    years_experience: str
    recommended_role: str
    score: int
