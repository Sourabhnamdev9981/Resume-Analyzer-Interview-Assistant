import json

from src.services.groq_service import get_groq_client
from src.utils.prompts import RESUME_ANALYSIS_PROMPT
from src.models.resume_schema import ResumeAnalysis


def analyze_resume(resume_text):

    client = get_groq_client()

    prompt = RESUME_ANALYSIS_PROMPT.format(resume_text=resume_text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", messages=[{"role": "user", "content": prompt}]
    )

    response_text = response.choices[0].message.content

    print("\nRAW RESPONSE:\n")
    print(response_text)
    print("\n")

    response_text = response_text.replace("```json", "").replace("```", "").strip()

    start = response_text.find("{")
    end = response_text.rfind("}") + 1

    json_text = response_text[start:end]

    data = json.loads(json_text)

    if "improvement_suggestions" in data:

        cleaned_suggestions = []

        for item in data["improvement_suggestions"]:

            if isinstance(item, dict):

                title = item.get("name", "")
                description = item.get("description", "")

                cleaned_suggestions.append(f"{title}: {description}")

            else:

                cleaned_suggestions.append(str(item))

        data["improvement_suggestions"] = cleaned_suggestions

    if "resume_score" in data and data["resume_score"] <= 10:
        data["resume_score"] *= 10

    return ResumeAnalysis(**data)
