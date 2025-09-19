PDF Converter
This Python script converts PDF files into plain text (.txt) and Word documents (.docx).
Requirements
Python 3.x
Libraries: pdfplumber, python-docx
Install the libraries using:
pip3 install pdfplumber python-docx
Usage
Run the script from the command line with the following format:
python3 pdf_converter.py <input_pdf> <output_txt> <output_docx>
Example:
python3 pdf_converter.py example.pdf output.txt output.docx
<input_pdf>: Path to the PDF you want to convert.
<output_txt>: Path where the plain text file will be saved.
<output_docx>: Path where the Word document will be saved.
