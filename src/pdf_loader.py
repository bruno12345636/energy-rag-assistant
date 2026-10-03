from pathlib import Path
from pypdf import PdfReader


def load_pdf(path):
    reader = PdfReader(path)

    pages = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            pages.append({
                "text": text,
                "page": page_number + 1,
                "source": Path(path).name
            })

    return pages


def load_all_pdfs(folder="data"):
    documents = []

    for path in Path(folder).glob("*.pdf"):
        documents.extend(load_pdf(path))

    return documents

def load_uploaded_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)

    pages = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            pages.append({
                "text": text,
                "page": page_number + 1,
                "source": uploaded_file.name
            })

    return pages