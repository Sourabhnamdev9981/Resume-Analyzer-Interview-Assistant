from src.utils.pdf_extractor import extract_text_from_pdf
from src.services.resume_analyzer import analyze_resume

pdf_path = input("Enter PDF path: ").strip().replace('"', "")

with open(pdf_path, "rb") as pdf_file:
    resume_text = extract_text_from_pdf(pdf_file)

analysis = analyze_resume(resume_text)

print("\nResume Score:")
print(analysis.resume_score)

print("\nSkill Categories:")
print(analysis.skill_categories)

print("\nStrengths:")
print(analysis.strengths)

print("\nWeaknesses:")
print(analysis.weaknesses)

print("\nMissing Skills:")
print(analysis.missing_skills)

print("\nSuggestions:")
print(analysis.improvement_suggestions)

print("\nHiring Assessment:")
print(analysis.hiring_assessment)