from pathlib import Path
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from all pages of a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Combined text from all pages.
    """
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found at: {pdf_path}")

    reader = PdfReader(str(path))
    all_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            all_text += text + "\n"

    return all_text.strip()


if __name__ == "__main__":
    pdf_file = "data/income_statement.pdf"
    try:
        extracted_text = extract_text_from_pdf(pdf_file)
        print("=== Extracted Text ===")
        print(extracted_text)
    except Exception as e:
        print(f"[ERROR] {e}")
