from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf_documents(folder_path: str):

    all_documents = []

    for pdf_file in Path(folder_path).glob("*.pdf"):

        loader = PyPDFLoader(str(pdf_file))

        documents = loader.load()

        all_documents.extend(documents)

    return all_documents