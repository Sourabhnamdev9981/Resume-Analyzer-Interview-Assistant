from src.utils.pdf_extractor import extract_text_from_pdf

pdf_path = input("Enter PDF path: ").strip().replace('"', "")

with open(pdf_path, "rb") as pdf_file:
    extracted_text = extract_text_from_pdf(pdf_file)

print("\n===== EXTRACTED TEXT =====\n")
print(extracted_text)
