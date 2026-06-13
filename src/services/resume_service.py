from src.utils.pdf_extractor import extract_text_from_pdf


def process_resume(uploaded_file):

    extracted_text = extract_text_from_pdf(uploaded_file)

    return {"resume_text": extracted_text}
