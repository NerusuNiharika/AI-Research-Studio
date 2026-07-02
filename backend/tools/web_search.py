from langchain_core.tools import tool
from langchain_tavily import TavilySearch

search = TavilySearch(
    max_results=2
)


@tool
def web_search_tool(query: str) -> str:
    """
    Search the web using Tavily and return relevant information.
    """

    results = search.invoke(query)

    if isinstance(results, list):

        return "\n\n".join(
            result.get("content", "")
            for result in results
        )

    return str(results)