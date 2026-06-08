from pydantic import BaseModel


class ResumeAnalysis(BaseModel):

    resume_score: int

    skill_categories: dict[str, list[str]]

    strengths: list[str]

    weaknesses: list[str]

    missing_skills: list[str]

    improvement_suggestions: list[str]

    hiring_assessment: str