from pypdf import PdfReader

def get_text_from_pdf(pdf_file):

    # Initialize PdfReader with the file-like object
    reader = PdfReader(pdf_file)

    text = ""
    # Extract text from each page
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()

    clean_text = text.replace("\n", " ")
    
    return clean_text

