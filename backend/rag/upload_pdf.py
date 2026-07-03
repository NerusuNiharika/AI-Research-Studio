import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore

from config.settings import (
    QDRANT_URL,
    QDRANT_API_KEY,
    COLLECTION_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

from rag.embeddings import embeddings


def upload_pdf_to_qdrant(pdf_path: str):

    # -----------------------------
    # Load PDF
    # -----------------------------

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    # -----------------------------
    # Split into Chunks
    # -----------------------------

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(documents)

    # -----------------------------
    # Connect to Existing Collection
    # -----------------------------

    vector_store = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=COLLECTION_NAME,
)

    # -----------------------------
    # Add Uploaded PDF Chunks
    # -----------------------------

    vector_store.add_documents(chunks)

    print(f"Successfully added {len(chunks)} chunks to '{COLLECTION_NAME}'")