import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_file) -> str:
    """
    Extract text from an uploaded PDF file.

    Args:
        pdf_file: Uploaded PDF file object

    Returns:
        str: Extracted text from the PDF
    """

    text = ""

    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf_document:
        text += page.get_text()

    pdf_document.close()

    return text.strip()
