RESUME_ANALYSIS_PROMPT = """
You are a Senior Technical Recruiter.

Analyze the resume.

Return ONLY valid JSON.

Do not return markdown.

Do not return explanations.

You MUST identify at least 3 weaknesses.

You MUST identify at least 3 missing industry skills.

You MUST provide at least 5 actionable improvement suggestions.

Be critical and realistic.

Do not assume the resume is perfect.

Even strong resumes have improvement opportunities.

Categorize skills into the most appropriate category.

Do not return a flat skill list.

Use this schema exactly:

{{
    "resume_score": integer,
    "skill_categories": {{
        "Programming": [],
        "Machine Learning": [],
        "Data Analysis": [],
        "Cloud": [],
        "Web Development": [],
        "Other": []
    }},
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "improvement_suggestions": [],
    "hiring_assessment": ""
}}
Resume:

{resume_text}
"""
INTERVIEW_QUESTIONS_PROMPT = """
You are a Senior Technical Interviewer.

Generate interview questions based on the candidate's resume.

Return ONLY valid JSON.

Schema:

{{
    "hr_questions": [],
    "technical_questions": [],
    "resume_based_questions": []
}}

Rules:

- Generate 5 HR questions.
- Generate 10 technical questions.
- Generate 10 resume-based questions.
- Questions must be personalized.
- Use projects, skills, and technologies from the resume.
- Do not generate generic questions unless necessary.

Resume:

{resume_text}
"""
