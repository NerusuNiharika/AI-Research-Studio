from langchain_qdrant import QdrantVectorStore

from config.settings import (
    COLLECTION_NAME,
    QDRANT_URL,
    QDRANT_API_KEY
)

from rag.embeddings import get_embeddings


retriever = None


def get_retriever():
    global retriever

    if retriever is None:
        vector_store = QdrantVectorStore.from_existing_collection(
            embedding=get_embeddings(),
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            collection_name=COLLECTION_NAME,
        )

        retriever = vector_store.as_retriever(
            search_kwargs={"k": 2}
        )

    return retriever


def retrieve_context(query: str) -> str:

    documents = get_retriever().invoke(query)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return context