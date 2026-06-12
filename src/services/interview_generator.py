import json

from src.services.groq_service import get_groq_client
from src.models.interview_schema import InterviewQuestions
from src.utils.prompts import INTERVIEW_QUESTIONS_PROMPT


def generate_interview_questions(resume_text):

    client = get_groq_client()

    prompt = INTERVIEW_QUESTIONS_PROMPT.format(resume_text=resume_text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", messages=[{"role": "user", "content": prompt}]
    )

    response_text = response.choices[0].message.content

    print("\nRAW RESPONSE:\n")
    print(response_text)

    start = response_text.find("{")
    end = response_text.rfind("}") + 1

    json_text = response_text[start:end]

    data = json.loads(json_text)

    return InterviewQuestions(
        hr_questions=data["hr_questions"],
        technical_questions=data["technical_questions"],
        resume_based_questions=data["resume_based_questions"],
    )
