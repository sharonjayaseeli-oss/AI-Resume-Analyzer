import pdfplumber
from docx import Document
import os


def extract_text(file_path):
    """
    Extract text from PDF or DOCX resume.
    """

    text = ""

    file_extension = os.path.splitext(file_path)[1].lower()

    # Read PDF
    if file_extension == ".pdf":
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            print("Error reading PDF:", e)

    # Read DOCX
    elif file_extension == ".docx":
        try:
            document = Document(file_path)
            for para in document.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            print("Error reading DOCX:", e)

    else:
        text = "Unsupported File Format"

    return text