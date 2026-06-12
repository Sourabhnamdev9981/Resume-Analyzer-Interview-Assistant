from pydantic import BaseModel


class InterviewQuestions(BaseModel):

    hr_questions: list[str]

    technical_questions: list[str]

    resume_based_questions: list[str]
