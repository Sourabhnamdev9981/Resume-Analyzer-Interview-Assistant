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

    print("\nJSON TEXT:\n")
    print(json_text)
    print("\n")

    data = json.loads(json_text)

    print("\nPARSED DATA:\n")
    print(data)
    print("\n")

    hr_questions = [
        item.get("question", str(item)) if isinstance(item, dict) else str(item)
        for item in data["hr_questions"]
    ]

    technical_questions = [
        item.get("question", str(item)) if isinstance(item, dict) else str(item)
        for item in data["technical_questions"]
    ]

    resume_based_questions = [
        item.get("question", str(item)) if isinstance(item, dict) else str(item)
        for item in data["resume_based_questions"]
    ]

    return InterviewQuestions(
        hr_questions=hr_questions,
        technical_questions=technical_questions,
        resume_based_questions=resume_based_questions,
    )
