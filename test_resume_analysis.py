from src.utils.pdf_extractor import extract_text_from_pdf
from src.services.resume_analyzer import analyze_resume


pdf_path = input("Enter PDF path: ").strip().replace('"', "")

with open(pdf_path, "rb") as pdf_file:

    resume_text = extract_text_from_pdf(pdf_file)

analysis = analyze_resume(resume_text)

print("\n")
print("=" * 50)
print("RESUME ANALYSIS")
print("=" * 50)
print("\n")

print(analysis)