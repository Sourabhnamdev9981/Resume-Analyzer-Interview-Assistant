from src.utils.pdf_extractor import extract_text_from_pdf
from src.services.interview_generator import generate_interview_questions

pdf_path = input("Enter PDF path: ").strip().replace('"', "")

with open(pdf_path, "rb") as pdf_file:
    resume_text = extract_text_from_pdf(pdf_file)

questions = generate_interview_questions(resume_text)

print("\n" + "=" * 50)
print("HR QUESTIONS")
print("=" * 50)

for i, question in enumerate(questions.hr_questions, start=1):
    print(f"{i}. {question}")

print("\n" + "=" * 50)
print("TECHNICAL QUESTIONS")
print("=" * 50)

for i, question in enumerate(questions.technical_questions, start=1):
    print(f"{i}. {question}")

print("\n" + "=" * 50)
print("RESUME-BASED QUESTIONS")
print("=" * 50)

for i, question in enumerate(questions.resume_based_questions, start=1):
    print(f"{i}. {question}")
