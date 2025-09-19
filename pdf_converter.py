import sys
import pdfplumber
from docx import Document

def pdf_to_text(pdf_path, txt_path):
    """Convert PDF to plain text file"""
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)

def pdf_to_docx(pdf_path, docx_path):
    """Convert PDF to Word document"""
    doc = Document()
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                doc.add_paragraph(page_text)
                doc.add_page_break()
    doc.save(docx_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 pdf_converter.py <pdf_file> <txt_file> <docx_file>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_txt = sys.argv[2]
    output_docx = sys.argv[3]

    pdf_to_text(input_pdf, output_txt)
    pdf_to_docx(input_pdf, output_docx)

    print(f"✅ Converted {input_pdf} → {output_txt} and {output_docx}")
