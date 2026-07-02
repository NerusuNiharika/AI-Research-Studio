from langchain_core.tools import tool

from rag.retriever import retrieve_context


@tool
def rag_tool(query: str) -> str:
    """
    Retrieve relevant information from the vector database.
    """

    return retrieve_context(query)