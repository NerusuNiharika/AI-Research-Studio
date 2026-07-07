from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_qdrant import QdrantVectorStore

from config.settings import (
    DOCS_FOLDER,
    COLLECTION_NAME,
    QDRANT_URL,
    QDRANT_API_KEY,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

from rag.embeddings import get_embeddings

from tools.pdf_loader import load_pdf_documents


documents = load_pdf_documents(DOCS_FOLDER)
print(f"Documents loaded: {len(documents)}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)


chunks = text_splitter.split_documents(
    documents
)

print(f"Chunks created: {len(chunks)}")
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=get_embeddings(),
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    collection_name=COLLECTION_NAME
)

print("Documents stored successfully in Qdrant.")