from langchain_qdrant import QdrantVectorStore

from config.settings import (
    COLLECTION_NAME,
    QDRANT_URL
)

from rag.embeddings import embeddings


vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url=QDRANT_URL,
    collection_name=COLLECTION_NAME
)


retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 2
    }
)


def retrieve_context(query: str) -> str:

    documents = retriever.invoke(query)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return context