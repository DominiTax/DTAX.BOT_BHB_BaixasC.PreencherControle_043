from PyPDF2 import PdfReader
def extract_pdf_text(pdf_path: str) -> str:
    try:
        pdf = PdfReader(pdf_path)
        text =''
        for page in pdf.pages:
            page_text = page.extract_text()
            text += page_text
        return text
    except Exception as e:
        raise e
if __name__ == "__main__":
    ...