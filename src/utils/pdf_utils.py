from PyPDF2 import PdfReader
def extract_pdf_text(pdf_path: str) -> str:
    try:
        pdf = PdfReader(pdf_path)
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            text += page_text
        return text
    except Exception as e:
        raise e
if __name__ == "__main__":
    text = extract_pdf_text(r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\RelatrioSERASA04Set2024-BentlyCNPJ01.128.902_0001-701.pdf')
    print(text)