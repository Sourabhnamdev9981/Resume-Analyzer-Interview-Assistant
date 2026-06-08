from src.services.groq_service import get_groq_client
from src.utils.prompts import RESUME_ANALYSIS_PROMPT


def analyze_resume(resume_text):

    client = get_groq_client()

    prompt = RESUME_ANALYSIS_PROMPT.format(
        resume_text=resume_text
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content